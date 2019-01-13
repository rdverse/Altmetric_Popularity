import os, sys, random, shutil
from os import listdir
import json
from pathlib import Path

def cleanFeatures(TRAINING):
	numOfFiles = 0
	publisherRemoved = 0
	authorsRemoved = 0
	journalRemoved = 0
	scopusRemoved = 0
	fileCounter = 0
	score = 0
	num = 0

	for folderName in os.listdir(TRAINING):
		for f in os.listdir(TRAINING + folderName): 
			with open(TRAINING + folderName + '\\' + f, encoding="ISO-8859-1") as file:
				data = json.load(file)

				# fileCounter += 1
				# if(fileCounter == 100000):
				# 	num += 100000
				# 	print(num)
				# 	fileCounter = 0

				if (data["altmetric_score"]["score"] is None):
					file.close()
					os.remove(TRAINING + folderName + '\\' + f)
					#print('removed: ', f, ' missing AUTHOR')
					# score += float(data["altmetric_score"]["score"])
					# authorsRemoved += 1

				elif ('authors' not in data['citation'] or data["citation"]["authors"] is None):
					file.close()
					os.remove(TRAINING + folderName + '\\' + f)
					#print('removed: ', f, ' missing AUTHOR')
					# score += float(data["altmetric_score"]["score"])
					# authorsRemoved += 1

				elif('journal' not in data['citation'] or data["citation"]["journal"] is None):
					file.close()
					os.remove(TRAINING + folderName + '\\' + f)
					#print('removed: ', f, ' missing JOURNAL')
					# score += float(data["altmetric_score"]["score"])
					# journalRemoved += 1

				elif('publisher' not in data['citation'] or data["citation"]["publisher"] is None):
					file.close()
					os.remove(TRAINING + folderName + '\\' + f)
					#print('removed: ', f, ' missing PUBLISHER')
					# score += float(data["altmetric_score"]["score"])
					# publisherRemoved += 1

				elif ('scopus_subjects' not in data['citation'] or data["citation"]["scopus_subjects"] is None):
					file.close()
					os.remove(TRAINING + folderName + '\\' + f)
					#print('removed: ', f, ' missing SCOPUS')
					# score += float(data["altmetric_score"]["score"])
					# scopusRemoved += 1

				elif('title' not in data['citation'] or data["citation"]["title"] is None):
					file.close()
					os.remove(TRAINING + folderName + '\\' + f)
					#print('removed: ', f, ' missing SCOPUS')
					# score += float(data["altmetric_score"]["score"])
					# titleRemoved += 1

			numOfFiles += 1

	print('FILES PROCESSED:    ', numOfFiles)
	# print('Authors Removed:    ', authorsRemoved, '   Percent: ', authorsRemoved / numOfFiles)
	# print('Journal Removed:    ', journalRemoved, '   Percent: ', journalRemoved / numOfFiles)
	# print('Publisher Removed:  ', publisherRemoved, '  Percent: ', publisherRemoved / numOfFiles)
	# print('Scopus Removed:     ', scopusRemoved, '    Percent: ', scopusRemoved / numOfFiles)

	# totalRemoved = authorsRemoved + journalRemoved + publisherRemoved + scopusRemoved

	# print('TOTAL REMOVED: ', totalRemoved)
	# print('TOTAL REMAINING: ', numOfFiles - totalRemoved)
	# print('AVERAGE ALTMETRIC SCORE FOR REMOVED FILES: ', totalRemoved / score)



if __name__ == '__main__':
	TRAINING = 'C:\\Users\\D\\Desktop\\randomSampleFinal\\'

	cleanFeatures(TRAINING)

