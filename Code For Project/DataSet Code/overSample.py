import os, sys, random, shutil
from os import listdir
import json
from pathlib import Path

def compareScores(TRAINING):
	zeroScore = 0
	midScore = 0
	avgAndAboveScore = 0.0
	totalFiles = 0

	for folderName in os.listdir(TRAINING):
		for f in os.listdir(TRAINING + folderName): 
			with open(TRAINING + folderName + '\\' + f, encoding="ISO-8859-1") as file:
				data = json.load(file)
				altmetScore = float(data["altmetric_score"]["score"])

				if(altmetScore == 0):
					zeroScore += 1
					file.close()

				elif(altmetScore > 0 and altmetScore < 3):
					midScore += 1
					file.close()

				elif(altmetScore >= 3 and altmetScore <= 10):
					avgAndAboveScore += 1
					file.close()

				else:
					file.close()

			totalFiles += 1

	print('TOTAL ARTICLES: ', totalFiles)
	print('TOTAL ARTICLES WITH SCORE OF 0:      ', zeroScore,  ' PERCENT: ', zeroScore / totalFiles)
	print('TOTAL ARTICLES WITH SCORE > 0 and < 3:   ', midScore, ' PERCENT: ', midScore / totalFiles)
	print('TOTAL ARTICLES WITH SCORE >= 3 and <= 10:      ', avgAndAboveScore, ' PERCENT: ', avgAndAboveScore / totalFiles)





if __name__ == '__main__':
	TRAINING = 'C:\\Users\\D\\Desktop\\newFolderV2\\'

	compareScores(TRAINING)