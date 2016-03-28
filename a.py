#!/usr/bin/env python3
import os
import sys
import time

args = []
validargs = ['a','c', 'h', 'f' ,'s=l', 's=s', 'd']
listall = False
toprint = ""
dtl = "."
for arg in sys.argv[1:]:
	if arg.startswith("-"):
		if arg[1:] in validargs:
			args.extend([arg])
		else:
			print("Invalid argument: " + arg)
			exit()
	elif os.path.isdir(arg):
		dtl = arg
	else:
		print("Invalid argument: " + arg)
if not 'c' in args and not 'f' in args:
	args.extend(['-d'])
def help():
	print("Usage: a [OPTION]")
	print("		-h: Display this")
	print("		-c: Compact, no size and keep use very little space.")
	print("		-d: Default, list file size and use space comfortably.")
	print("		-s=l: Sort from largest to smallest.")
	print("		-s=s: Sort from smallest to largest.")
	print("		-f: List every attribute and use a lot of space.")
	sys.exit()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    CYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def byte_to(b):
	if b <= 1000:
		return str(b) + "B"
	elif b > 1000 and b < (1000000):
		return str(round(b / 1000,1)) + "KB"
	elif b > (1000000) and b < (1000000000):
		return str(round(b / 1000000,1)) + "MB"
	elif b > (1000000000) and b < (1000000000000):
		return str(round(b / 1000000000, 1)) + "GB"

os.chdir(dtl)
FILES = os.listdir()
for arg in args:
	if arg == "-a":
		listall = True
	elif arg == "-h":
		help()
	elif arg.startswith("-s="):
		directory = ""
		pairs = []
		for file in FILES:
			if os.path.isfile(file):
				if not file.startswith("."):
					location = os.path.join(directory, file)
					size = os.path.getsize(location)
					pairs.append((size, file))
				else:
					if listall == True:
						location = os.path.join(directory, file)
						size = os.path.getsize(location)
						pairs.append((size, file))
			else:
				if file.startswith("."):
					if listall == True:
						location = os.path.join(directory, file)
						size = os.path.getsize(location)
						pairs.append((size, file))
				else:
					location = os.path.join(directory, file)
					size = os.path.getsize(location)
					pairs.append((size, file))

		# Sort list of tuples by the first element, size.
		pairs.sort(key=lambda s: s[0])
		if arg == "-s=l":
			pairs.reverse()
		elif arg == "-s=s":
			pass
		FILES = []
		for FILE in pairs:
      			FILES.extend([FILE[1]])
	elif arg == "-c":
		for FILE in FILES:
			if os.path.isfile(str(FILE)):
				if not str(FILE).startswith("."):
					print(bcolors.OKGREEN + str(FILE) + bcolors.ENDC, end='  ')
				else:
                          		if listall == True:
                                		print(bcolors.OKGREEN + str(FILE) + bcolors.ENDC, end='  ')
			else:
				if str(FILE).startswith("."):
					try:
						if listall == True:
							print(bcolors.WARNING + str(FILE) + bcolors.ENDC, end='  ')
					except:
						pass
				else:
					print(bcolors.WARNING + str(FILE) + bcolors.ENDC, end='  ')
		exit();
	elif arg == "-d":
		for FILE in FILES:
			if os.path.isfile(str(FILE)):
				if not str(FILE).startswith("."):
					print(byte_to(os.path.getsize(str(FILE))) + "	" + bcolors.OKGREEN + FILE + bcolors.ENDC)
				else:
                          		if listall == True:
                                		print(byte_to(os.path.getsize(str(FILE))) + "	" + bcolors.OKGREEN + FILE + bcolors.ENDC)
			else:
				if str(FILE).startswith("."):
					try:
						if listall == True:
							print("    	" + bcolors.WARNING + FILE + bcolors.ENDC)
					except:
						pass
				else:
					print("    	" + bcolors.WARNING + FILE + bcolors.ENDC)
		exit();

	elif arg == "-f":
		for FILE in FILES:
			if os.path.isfile(str(FILE)):
				if not str(FILE).startswith("."):
					print(bcolors.CYAN + time.ctime(os.path.getmtime(str(FILE))) + bcolors.ENDC + " " + byte_to(os.path.getsize(str(FILE))) + "	" + bcolors.OKGREEN + FILE + bcolors.ENDC)
				else:
                          		if listall == True:
                                		print(bcolors.CYAN + time.ctime(os.path.getmtime(str(FILE))) + bcolors.ENDC + " " + byte_to(os.path.getsize(str(FILE))) + "	" + bcolors.OKGREEN + FILE + bcolors.ENDC)
			else:
				if str(FILE).startswith("."):
					try:
						if listall == True:
							print(bcolors.CYAN + time.ctime(os.path.getmtime(str(FILE))) + bcolors.ENDC + "    	" + bcolors.WARNING + FILE + bcolors.ENDC)
					except:
						pass
				else:
					print(bcolors.CYAN + time.ctime(os.path.getmtime(str(FILE))) + bcolors.ENDC +  "    	" + bcolors.WARNING + FILE + bcolors.ENDC)
		exit();
