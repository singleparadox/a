#!/usr/bin/env python3
import operator
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
if not '-c' in args and not '-f' in args:
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

def byte_to(original, decimals):
	magnitudes = "K", "M", "G", "T", "P", "E"

	value, unit = original, ""
	for magnitude in magnitudes:
		if value < 1000:
			break

		value /= 1000
		unit = magnitude

	return "{:.{}f}{}B".format(value, decimals, unit)

os.chdir(dtl)
FILES = os.listdir()
for arg in args:
	if arg == "-a":
		listall = True
	elif arg == "-h":
		help()
	elif arg.startswith("-s="):
		files_with_size = [(os.path.getsize(file), file) for file in FILES]
		# Sort files by size, reverse order if we're using "-s=l" (sort=largest first)
		files_with_size.sort(key=operator.itemgetter(0), reverse=arg == '-s=l')
		FILES = [file for size, file in files_with_size]

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
		print()  # Ensure output ends in a newline
		exit();
	elif arg == "-d":
		for FILE in FILES:
			if os.path.isfile(str(FILE)):
				if not str(FILE).startswith("."):
					print(byte_to(os.path.getsize(str(FILE)), 1) + "	" + bcolors.OKGREEN + FILE + bcolors.ENDC)
				else:
					if listall == True:
						print(byte_to(os.path.getsize(str(FILE)), 1) + "	" + bcolors.OKGREEN + FILE + bcolors.ENDC)
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
					print(bcolors.CYAN + time.ctime(os.path.getmtime(str(FILE))) + bcolors.ENDC + " " + byte_to(os.path.getsize(str(FILE)), 0) + "	" + bcolors.OKGREEN + FILE + bcolors.ENDC)
				else:
					if listall == True:
						print(bcolors.CYAN + time.ctime(os.path.getmtime(str(FILE))) + bcolors.ENDC + " " + byte_to(os.path.getsize(str(FILE)), 0) + "	" + bcolors.OKGREEN + FILE + bcolors.ENDC)
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
