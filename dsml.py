# !/usr/bin/python

# dsml - Dataset Sort for Machine Learning
# Description: Organize randomly selected files from a folder into training, testing and validation subfolder according to user specified percentages.

#Copyright (c) 2018 Javier O. Cordero Pérez <javier@imaginary.tech>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#f this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

# Imports
import argparse
import random
import os
from os import walk

# Argument parsing
parser = argparse.ArgumentParser(prog="dsml", description='Organize randomly selected files from a folder into training, testing and validation subfolder according to user specified percentages.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('integers', metavar='N', type=int, nargs="3", help='specify percentages in which to randomly organize files')
parser.add_argument('-R', dest='recursive', action='store_const', const=sum, default=max, help='grab files from subdirectories, recursively')

args = parser.parse_args()
print(args.recursive(args.integers))

# Arguments
trainPercentage = 60
testPercentage = 20
validatePercentage = 20
# Dev: use dictionaries instead
# percentages = ( , , )
recursive = False
move = False
inputPath = "./"
outputPath = "./"

# Set defaults for non-specified values
if trainPercentage is None:
	trainPercentage = 60
	testPercentage = 20
	validatePercentage = 20
elif testPercentage is None:
	remainder = 100-trainPercentage
	testPercentage = remainder/2
	validatePercentage = remainder/2
elif validatePercentage is None:
	validatePercentage = 100-(trainPercentage+testPercentage)

# Validate
# Validate percentages
if trainPercentage<0 or testPercentage<0 or validatePercentage<0:
	print("Invalid percentages specified. Exiting...")
	exit()

# Generate files list
files = []
for (dirpath, dirnames, filenames) in walk(inputPath):
    # Get all filenames in a folder
    files.extend(filenames)
    # Prevent from getting filenames from sub-folders unless recursive is specified
    if (not recursive):
    	break

# Randomize generated file list
shuffledFiles = files #.split('\n')
random.shuffle(shuffledFiles)

# Determine size of train, test and validate size percentages.
totalFiles = len(shuffledFiles)
trainSize = totalFiles//trainPercentage
testSize = totalFiles//testPercentage
validateSize = totalFiles//validatePercentage

# Split selected files three sets
lastTest = trainSize+testSize
train_data = shuffledFiles[:trainSize]
test_data = shuffledFiles[trainSize:lastTest]
validate_data = shuffledFiles[lastTest:]

# Make directories to contain sets if directories don't exist.
outPaths = [outputPath+"/train", outputPath+"/test", outputPath+"/validate"]
for path in outPaths:
	if not os.path.exists(path):
	    os.makedirs(path)

# If directories have pre-existing content, ask the user to delete contents.
exitFlag = False
# ...

# If user didn't choose to stop the program,
if not exitFlag:
	# proceed to copy files into the sub-folders 
	print("Copying files... Not!")
	#...

# End script
exit()
