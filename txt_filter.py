import re
filename = "test.txt"
#outfiles = "out"+str(i)+".txt"


def fkeep():
	number=0
	outfiles = "out"+str(number)+".txt"
	while True:
		keep = input('What part do you want to keep? (else type done) ')
		with open (filename,"r") as f:
			for line in f.readlines():
				if keep in line:
					keepdone = (line.strip())
					with open(outfiles, 'a') as w:
						w.write(keepdone+'\n')
					print(keepdone)
					number = number + 1
			if keep == 'done':
				break
	return keepdone

def fremovetags():
	qremovetags = input('Would you like to remove tags? (y/n) ')
	if qremovetags == 'y':
		with open ('out0.txt',"r") as r:
			for line in r.readlines():
				cleanr = re.compile('<.*?>')
				notags = re.sub(cleanr, '', line)
				with open(outfiles, 'a') as w:
					w.write(notags)
					print(notags)
	elif qremovetags == 'n':
		notags = keepdone
		return notags

def removedat():
	while True:
		remove = input('What would you like to remove? (else type done) ')
		with open ('out0.txt',"r") as r:
			for line in r.readlines():
				fixedline = line.replace(remove, "")
				print(fixedline)
				with open(outfiles, 'a') as w:
					w.write(fixedline)
		if remove == 'done':
			break
	return fixedline


keepdone = fkeep()
notags = fremovetags()
fixedline = removedat()




#remove everything between:
#keep words between:
            #for m_word in message:
             #   if m_word.startswith('<p>='):
              #      utf8_emoji = m_word