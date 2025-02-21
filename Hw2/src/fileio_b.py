from tqdm import tqdm
import numpy as np

# from my_quantize import DequantizeFP, MantissaFP, ScaleFactor
from pcmfile import *
from quantize import (
    DequantizeFP,
    MantissaFP,
    ScaleFactor,
    vDequantize,
    vDequantizeUniform,
    vMantissa,
    vQuantizeUniform,
)


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
    inFile.Close(codingParams)
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
                DequantizeFP(ScaleFactor(x), MantissaFP(x, ScaleFactor(x))) for x in data[iCh]
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


if __name__ == "__main__":
    # create the audio file objects of the appropriate audioFile type
    inFile = PCMFile("../audio/input.wav")
    # open input file and get its coding parameters
    codingParams = inFile.OpenForReading()
    # set additional coding parameters that are needed for encoding/decoding
    codingParams.nSamplesPerBlock = 1024

    # uniform_quantize(inFile, codingParams)
    # floatPoint_quantize(inFile, codingParams)
    blockFloatPoint_quantize(inFile, codingParams)
