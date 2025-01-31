import numpy as np
from os.path import dirname

# from my_quantize import DequantizeFP, MantissaFP, ScaleFactor
from pcmfile import PCMFile
from quantize import (
    DequantizeFP,
    MantissaFP,
    ScaleFactor,
    vDequantize,
    vDequantizeUniform,
    vMantissa,
    vQuantizeUniform,
)
from window import SineWindow
from mdct import MDCT, IMDCT


def uniform_quantize(data, nBits):
    return vDequantizeUniform(vQuantizeUniform(data, nBits), nBits)


def floatpoint_quantize(data, nScaleBits=3, nMantBits=5):
    output = []
    for x in data:
        scale = ScaleFactor(x, nScaleBits, nMantBits)
        mantissa = MantissaFP(x, scale, nScaleBits, nMantBits)
        output.append(DequantizeFP(scale, mantissa, nScaleBits, nMantBits))
    return np.array(output)


def blockFloatPoint_quantize(data, blockSize=16, nScaleBits=3, nMantBits=5):
    output = np.zeros_like(data).reshape(-1, blockSize)
    for n, sub in enumerate(data.reshape(-1, blockSize)):
        maxMagnitude = np.max(np.abs(sub))
        scale = ScaleFactor(maxMagnitude, nScaleBits, nMantBits)
        mantissaVec = vMantissa(sub, scale, nScaleBits, nMantBits)
        output[n] = vDequantize(scale, mantissaVec, nScaleBits, nMantBits)
    output = output.reshape(-1)
    return output


def overlapAndAdd_coding(inFile_path, N, use_mdct=True, quant_type=None):
    # create the audio file objects of the appropriate audioFile type
    inFile = PCMFile(inFile_path)
    # open input file and get its coding parameters
    codingParams = inFile.OpenForReading()
    codingParams.nSamplesPerBlock = N

    # 2.a, 2.b, 2.c
    outFile = PCMFile(
        f"{dirname(inFile_path)}/output_b{codingParams.nSamplesPerBlock}_q{quant_type}.wav"
    )
    outFile.OpenForWriting(codingParams)

    # create two data arrays for processing
    priorBlock = np.zeros((codingParams.nChannels, codingParams.nSamplesPerBlock))
    overlapAndAdd = np.zeros((codingParams.nChannels, codingParams.nSamplesPerBlock))
    # Read the input file and pass its data to the output file to be written
    while True:
        data = inFile.ReadDataBlock(codingParams)
        if not data:
            break  # we hit the end of the input file
        for iCh in range(codingParams.nChannels):
            # 2.a) a. concatenate the current data block with priorBlock (save the current block)
            data_concat = np.concat((priorBlock[iCh], data[iCh]))
            priorBlock[iCh] = data[iCh]
            # 2.a) b. window this concatenated block with a Sine window
            data_windowed = SineWindow(data_concat)

            # 2.b) MDCT
            data_tranformed = (
                MDCT(
                    data_windowed,
                    codingParams.nSamplesPerBlock,
                    codingParams.nSamplesPerBlock,
                )
                if use_mdct
                else data_windowed
            )

            # 2.c) quantization
            match quant_type:
                case None:
                    data_quantized = data_tranformed
                case "MT8":
                    data_quantized = uniform_quantize(data_tranformed, 8)
                case "FP35":
                    data_quantized = floatpoint_quantize(data_tranformed)
                case "BFP35":
                    data_quantized = blockFloatPoint_quantize(data_tranformed)
                case _:
                    raise NotImplementedError

            # 2.b) IMDCT
            data_prime = (
                IMDCT(
                    data_quantized,
                    codingParams.nSamplesPerBlock,
                    codingParams.nSamplesPerBlock,
                )
                if use_mdct
                else data_quantized
            )

            # 2.a) c. window again
            data_rewindowed = SineWindow(data_prime)
            # 2.a) d. add the left half to overlapAndAdd (save the right half)
            result = (
                overlapAndAdd[iCh] + data_rewindowed[: codingParams.nSamplesPerBlock]
            )
            overlapAndAdd[iCh] = data_rewindowed[codingParams.nSamplesPerBlock :]
            # 2.a) e. set data to the result
            data[iCh] = result

        outFile.WriteDataBlock(data, codingParams)
    # end loop over reading/writing the blocks

    # close the files
    inFile.Close(codingParams)
    outFile.Close(codingParams)


if __name__ == "__main__":
    inFile_path = "../audio/input.wav"
    for N in [512, 1024, 2048]:
        overlapAndAdd_coding(inFile_path, N, use_mdct=True, quant_type="MT8")
        overlapAndAdd_coding(inFile_path, N, use_mdct=True, quant_type="FP35")
