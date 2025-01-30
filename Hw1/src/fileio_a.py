from pcmfile import *


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
    outFile.WriteDataBlock(data, codingParams)
# end loop over reading/writing the blocks

# close the files
inFile.Close(codingParams)
outFile.Close(codingParams)
