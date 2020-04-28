#!/usr/bin/env python

# Randomly prints a phrase from the text
import random
import os
import pickle

script_dir = os.path.dirname(__file__)

PICKLE_FILENAME = 'text.pkl'
RAW_TEXT_FILENAME = 'full-text.txt'

def getTextDict():
	text = open(os.path.join(script_dir, RAW_TEXT_FILENAME), 'r')
	result = {}
	currentHeader = ''

	for line in text:
		line = line.strip()
		if (len(line) > 0):
			firstSpace = line.find(' ')
			if (firstSpace > 0 and line[firstSpace - 1] == '.'):
				if (line[firstSpace - 2].isdigit()):
					result[currentHeader].append(line[firstSpace + 1 :])
				else:
					currentHeader = line[firstSpace + 1 :]
					result[currentHeader] = []
			else:
				endIdx = len(result[currentHeader]) - 1
				result[currentHeader][endIdx] += ' ' + line
	
	return result

def randListVal(list):
	return list[random.randint(0, len(list) - 1)]

def pickleObj(textDict, filename):
	f = open(filename, 'wb')
	pickle.dump(textDict, f)
	f.close()

def isPickled(filename):
	return True if os.path.isfile(filename) else False

def unPickle(filename):
	f = open(filename, 'rb')
	return pickle.load(f)

if __name__ == '__main__':
	textDict = {}
	if (isPickled(PICKLE_FILENAME)):
		textDict = unPickle(PICKLE_FILENAME)
	else:
		textDict = getTextDict()
		pickleObj(textDict, PICKLE_FILENAME)

	randKey = randListVal(textDict.keys())
	randValue = randListVal(textDict[randKey])

	print('From ' + randKey + ' \n' + randValue)
