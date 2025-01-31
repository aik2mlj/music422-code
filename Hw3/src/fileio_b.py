import numpy as np

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


def uniform_quantize(inFile, codingParams):
    outFile_uq = PCMFile("../audio/uq.wav")

    # open the output file for writing, passing needed format/data parameters
    outFile_uq.OpenForWriting(codingParams)

    # Read the input file and pass its data to the output file to be written
    while True:
        data = inFile.ReadDataBlock(codingParams)
        if not data:
            break  # we hit the end of the input file
        nBits = 8
        data_uq = np.zeros_like(data)
        for iCh in range(codingParams.nChannels):
            # data[iCh]: (1024,)
            data_uq[iCh] = vDequantizeUniform(vQuantizeUniform(data[iCh], nBits), nBits)

        outFile_uq.WriteDataBlock(data_uq, codingParams)
    # end loop over reading/writing the blocks

    # close the files
    outFile_uq.Close(codingParams)


def floatPoint_quantize(inFile, codingParams):
    # open the output file for writing, passing needed format/data parameters
    outFile_fpq = PCMFile("../audio/fpq.wav")
    outFile_fpq.OpenForWriting(codingParams)

    # Read the input file and pass its data to the output file to be written
    while True:
        data = inFile.ReadDataBlock(codingParams)
        if not data:
            break  # we hit the end of the input file
        data_fpq = np.zeros_like(data)
        for iCh in range(codingParams.nChannels):
            # data[iCh]: (1024,)
            data_fpq[iCh] = [
                DequantizeFP(ScaleFactor(x), MantissaFP(x, ScaleFactor(x)))
                for x in data[iCh]
            ]

        outFile_fpq.WriteDataBlock(data_fpq, codingParams)
    # end loop over reading/writing the blocks

    # close the files
    outFile_fpq.Close(codingParams)


def blockFloatPoint_quantize(inFile, codingParams):
    # open the output file for writing, passing needed format/data parameters
    for N in [16]:
        outFile = PCMFile(f"../audio/bfpq_{N}.wav")
        outFile.OpenForWriting(codingParams)

        # Read the input file and pass its data to the output file to be written
        while True:
            data = inFile.ReadDataBlock(codingParams)
            if not data:
                break  # we hit the end of the input file
            output = np.zeros_like(data)
            for iCh in range(codingParams.nChannels):
                # data[iCh]: (1024,)
                output_iCh = np.zeros_like(data[iCh]).reshape(-1, N)
                # print(output_iCh.shape)
                for n, sub in enumerate(data[iCh].reshape(-1, N)):
                    maxMagnitude = np.max(np.abs(sub))
                    scale = ScaleFactor(maxMagnitude)
                    mantissaVec = vMantissa(sub, scale)
                    output_iCh[n] = vDequantize(scale, mantissaVec)
                output[iCh] = output_iCh.reshape(-1)
                # print(output[iCh].shape)

            outFile.WriteDataBlock(output, codingParams)
        # end loop over reading/writing the blocks

        # close the files
        outFile.Close(codingParams)


def overlap_add(inFile, codingParams, use_mdct=True, quant_type=None):
    # 2.a, 2.b, 2.c
    outFile_uq = PCMFile("../audio/overlap_add.wav")
    outFile_uq.OpenForWriting(codingParams)

    # create two data arrays for processing
    priorBlock = np.zeros((codingParams.nChannels, codingParams.nSamplesPerBlock))
    overlapAndAdd = np.zeros((codingParams.nChannels, codingParams.nSamplesPerBlock))
    # Read the input file and pass its data to the output file to be written
    while True:
        data = inFile.ReadDataBlock(codingParams)
        if not data:
            break  # we hit the end of the input file
        for iCh in range(codingParams.nChannels):
            # data[iCh]: (1024,)
            # 2.a) a. concatenate the current data block with priorBlock (save the current block)
            data_concat = np.concat((priorBlock[iCh], data[iCh]))  # (2048,)
            priorBlock[iCh] = data[iCh]
            # 2.a) b. window this concatenated block with a Sine window
            data_windowed = SineWindow(data_concat)

            # 2.b) MDCT & IMDCT
            if use_mdct:
                data_tranformed = MDCT(
                    data_windowed,
                    codingParams.nSamplesPerBlock,
                    codingParams.nSamplesPerBlock,
                )
                data_prime = IMDCT(
                    data_tranformed,
                    codingParams.nSamplesPerBlock,
                    codingParams.nSamplesPerBlock,
                )
            else:
                data_prime = data_windowed

            # 2.a) c. window again
            data_rewindowed = SineWindow(data_prime)
            # 2.a) d. add the left half to overlapAndAdd (save the right half)
            result = (
                overlapAndAdd[iCh] + data_rewindowed[: codingParams.nSamplesPerBlock]
            )
            overlapAndAdd[iCh] = data_rewindowed[codingParams.nSamplesPerBlock :]
            # 2.a) e. set data to the result
            data[iCh] = result

        outFile_uq.WriteDataBlock(data, codingParams)
    # end loop over reading/writing the blocks

    # close the files
    outFile_uq.Close(codingParams)


if __name__ == "__main__":
    # create the audio file objects of the appropriate audioFile type
    inFile = PCMFile("../audio/input.wav")
    # open input file and get its coding parameters
    codingParams = inFile.OpenForReading()
    # set additional coding parameters that are needed for encoding/decoding
    codingParams.nSamplesPerBlock = 1024

    # uniform_quantize(inFile, codingParams)
    # floatPoint_quantize(inFile, codingParams)
    # blockFloatPoint_quantize(inFile, codingParams)
    overlap_add(inFile, codingParams)
    inFile.Close(codingParams)
