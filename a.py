import glob 
import string
import os

def FindAll(path):
	return glob.glob(path + "/*/*.txt");

def IsAnswerN(line):
	p = string.find(line, ": N");
	return p != -1;

def ChangeAnswer(fileName, line):
	read = open(fileName)
	write = open(fileName + "2", "w")
	for tmpLine in read:
		if(line == tmpLine) :
			write.write(line[0 : len(line)-2] + "M" + "\n")
		else :
			write.write(tmpLine)
	read.close()
	write.close()
	os.rename(fileName+"2", fileName);

def main():
	all = FindAll("cleaneddata")
	for file in all:
		f = open(file)
		for line in f:
			if IsAnswerN(line):
				f.close();
				ChangeAnswer(file, line)
				break;
	
main()





