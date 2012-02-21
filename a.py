import glob 

def FindAll(path):
	return glob.glob(path + "/*/*");

def IsAnswerN(line)
	return string.find(line, ": N") != -1;

def ChangeAnswer(fileName, line):
	f = open(file);
	f[line][len(f[line]-1] = 'M';

def main():
	all = FindAll("cleaneddata")
	for file in all:
		f = open(file)
		for line in f:
			if(IsAnswerN(line)):
				ChangeAnswer(file, line);
	
main()





