import glob 
import string

def FindAll(path):
	return glob.glob(path + "/*/*");

def IsAnswerN(line):
	return string.find(line, ": N") != -1;

def ChangeAnswer(fileName, line):
	read = open(fileName)
	write = open(fileName, "w")
	for tmpLine in read:
		if(line == tmpLine) :
			write.write(line[0, len(line)-2] + "M")
		else :
			write.write(tmpline)

def main():
	all = FindAll("cleaneddata")
	for file in all:
		f = open(file)
		for line in f:
			if(IsAnswerN(line)):
				ChangeAnswer(file, line)
	
main()





