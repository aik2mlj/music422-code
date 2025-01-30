from pcmfile import *
from quantize import vQuantizeUniform, vDequantizeUniform


# create the audio file objects of the appropriate audioFile type
inFile = PCMFile("input.wav")
outFile = PCMFile("output.wav")

# open input file and get its coding parameters
codingParams = inFile.OpenForReading()

# set additional coding parameters that are needed for encoding/decoding
codingParams.nSamplesPerBlock = 1024

# open the output file for writing, passing needed format/data parameters
outFile.OpenForWriting(codingParams)

# Read the input file and pass its data to the output file to be written
while True:
    data = inFile.ReadDataBlock(codingParams)
    if not data:
        break  # we hit the end of the input file
    nBits = 4
    # nBits = 6
    # nBits = 8
    # nBits = 10
    # nBits = 12
    for iCh in range(codingParams.nChannels):
        data[iCh] = vDequantizeUniform(vQuantizeUniform(data[iCh], nBits), nBits)
    outFile.WriteDataBlock(data, codingParams)
# end loop over reading/writing the blocks

# close the files
inFile.Close(codingParams)
outFile.Close(codingParams)
