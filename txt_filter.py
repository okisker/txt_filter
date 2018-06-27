import re

filename = "test.txt"
keep = input('What part do you want to keep? ')
remove = input('What would you like to remove? ')
remove2 = input('Anything else we can remove? ')

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def removedat(line):
	fixedline = line.replace(remove, "")
	return fixedline

def removedat2(line):
	fixedline = line.replace(remove2, "")
	return fixedline

with open (filename,"r") as f:
	for line in f.readlines():
		if keep in line:
			line = (line.strip())
			cleantext = cleanhtml(line)
			fixedline = removedat(cleantext)
			finalline = removedat2(fixedline)
			print(finalline)

#remove everything between:
#keep words between: