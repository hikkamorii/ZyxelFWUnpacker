#!/usr/bin/python
import os
import sys

class colors:
	HIKKA = '\033[0;35m'
	WARN = '\033[93m\033[1m'
	FAIL = '\033[91m\033[1m'
	UND = '\033[4m'
	OK = '\033[92m\033[1m'
	R = '\033[0m'

foundfiles =0
filefound = 0
files=0

print colors.HIKKA + "Zyxel firmware extractor pack by hikkamorii." + colors.R
print "This python script is for splitting files from one big file extracted using onefile.sh (Bundled with this script)"
if len(sys.argv) != 2:
	print colors.FAIL + " [X] " + colors.R + " File not specified."
else:
	if os.path.exists(sys.argv[1]):
			with open(sys.argv[1]) as input_data:
				for line in input_data:
					wLine = list(line)
					if (line.strip() == '&&*&&en**&**'):
						print colors.WARN + " [!] " + colors.R + " &&*&&en**&** Found. Ignoring."
					if (wLine[0] == '&' and wLine[1] == "*" and wLine[2] == "#" and wLine[3] == "@"):
						filefound = 1
						filename = ''
						counter = 4
						while wLine[counter] != "@":
							filename = filename + wLine[counter] 
							counter += 1
						foundfiles += 1
						print colors.OK + " [V] " + colors.R + " Found file " + filename + "; " + colors.UND + "file #" + str(foundfiles) + colors.R;
						try:
							os.remove(filename)
						except OSError:
							pass
					if(filefound):
						with open("files/" + filename, "a") as file:
							if len(line)>4:
								if (wLine[0] != '&' and wLine[1] != "*" and wLine[2] != "#" and wLine[3] != "@"):  #&*#@
									file.write(line)
	else:
		print colors.FAIL + " [X] " + colors.R + " Error oppening file."
