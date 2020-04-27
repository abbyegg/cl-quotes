# Randomly prints a phrase in the array
import random
import os
script_dir = os.path.dirname(__file__)

def getTextDict():
	text = open(os.path.join(script_dir, 'full-text.txt'), 'r')
	result = {}
	currentHeader = ''

	for line in text:
		line = line.strip()
		if (len(line) > 0):
			# 1st case, it's a header
			firstSpace = line.find(' ')
			if (firstSpace > 0 and line[firstSpace - 1] == '.'):
				if (line[firstSpace - 2].isdigit()):
					# add to list
					result[currentHeader].append(line[firstSpace + 1 :])
				else:
					# new header
					currentHeader = line[firstSpace + 1 :]
					result[currentHeader] = []
			else:
				# continuing current phrase
				result[currentHeader][len(result[currentHeader]) - 1] += ' ' + line
	
	return result

def getRandomListValue(lst):
	return lst[random.randint(0, len(lst) - 1)]

if __name__ == '__main__':
	textDict = getTextDict()
	randKey = getRandomListValue(textDict.keys())
	randValue = getRandomListValue(textDict[randKey])
	print('From ' + randKey + ' \n' + randValue)
