import os, sys, random, shutil
from os import listdir
import json
from pathlib import Path

#this seperates each json object into it's own file and names it a number
def seperateJson(RANDOM_SAMPLE_PATH, SEP_JSON_PATH):
	count = 0 			
	for filename in os.listdir(RANDOM_SAMPLE_PATH):
		with open(RANDOM_SAMPLE_PATH + filename, encoding="ISO-8859-1") as openf:
			for line in openf:
				count += 1

				#name the new file the count and create a new file named the count
				newFile = open(SEP_JSON_PATH + '\\' + str(count) + '.txt', 'w+') 
				newFile.write(line)
				newFile.write('\n')
				newFile.close()

				#call function to convert to .json
				convertToJson(SEP_JSON_PATH, str(count) + '.txt') 

#converts to each selected random sample and seperates into own .json file
def convertToJson(SEP_JSON_PATH, newfile):
	#changes the stem of the file name
	newName = Path(newfile).stem + ".json"
	os.rename(SEP_JSON_PATH + '\\' + newfile, SEP_JSON_PATH + '\\' + newName)



if __name__ == '__main__':
	RANDOM_SAMPLE_PATH = 'C:\\Users\\D\\Desktop\\randomSampleData\\'
	SEP_JSON_PATH = 'C:\\Users\\D\\Desktop\\finalSample\\'

	seperateJson(RANDOM_SAMPLE_PATH, SEP_JSON_PATH)

