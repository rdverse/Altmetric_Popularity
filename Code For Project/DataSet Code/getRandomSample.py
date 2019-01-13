import os, sys, random, shutil
from os import listdir
from pathlib import Path
import json

#remove all empty files in keys folder
def checkEmptyFiles(FILEPATH):
	for filename in os.listdir(FILEPATH):
		if os.stat(FILEPATH + filename).st_size == 0:
			print('removing directory: ', filename)
			os.rmdir(FILEPATH + filename)


#calculates number of all data files to choose % for a sample
def getNumOfFiles(FILEPATH):
	num_files = 0
	for foldername in os.listdir(FILEPATH):
		for f in os.listdir(FILEPATH + foldername): 
			num_files += 1

	return num_files


def selectRandomSample(FILEPATH, RANDOM_SAMPLE_PATH):
	#call function to get calc number of all files
	num_files = getNumOfFiles(FILEPATH)

	#get 10% of the full data to sample from files
	sampleRange = int(round(num_files * .20))

	#a way to check for dupes so no sample replacement
	chosenFiles = []

	for i in range(sampleRange):
		#randomly choose a folder in path
		foldername = random.choice(os.listdir(FILEPATH))
		print('folder name: ' ,foldername)

		if os.stat(FILEPATH + foldername).st_size > 0:
			#randomly choose a file in chosen folder
			random_file = random.choice(os.listdir(FILEPATH + foldername))
			print('randdom file: ', random_file)

			if random_file not in chosenFiles:
				chosenFiles.append(random_file)
				#move samples to random samples folder
				shutil.move(FILEPATH + foldername + '\\'+ random_file, RANDOM_SAMPLE_PATH)
			else:
				print('file: ', random_file, 'in folder already')
		else:
			os.rmdir(FILEPATH + foldername)


if __name__ == '__main__':
	FILEPATH = 'C:\\Users\\D\\Desktop\\getSamp\\'
	RANDOM_SAMPLE_PATH = 'C:\\Users\\D\\Desktop\\randomSampleData\\'
	checkEmptyFiles(FILEPATH)
	selectRandomSample(FILEPATH, RANDOM_SAMPLE_PATH)