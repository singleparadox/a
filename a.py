#!/usr/bin/env python3
import operator
import os
import stat
import sys
import time

from datetime import datetime


def help():
	print("Usage: a [OPTION]")
	print("		-h: Display this")
	print("		-c: Compact, no size and keep use very little space.")
	print("		-d: Default, list file size and use space comfortably.")
	print("		-s=l: Sort from largest to smallest.")
	print("		-s=s: Sort from smallest to largest.")
	print("		-f: List every attribute and use a lot of space.")
	exit()


class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	CYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	GRAY = '\033[90m'
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


def size_color(size):
	if size < 1000:
		return bcolors.GRAY
	elif size < 1000000:
		return bcolors.ENDC
	elif size < 1000000000:
		return bcolors.WARNING
	else:
		return bcolors.FAIL


def print_file(format_string, fname, **print_keywords):
	file_stats = os.lstat(fname)

	if stat.S_ISREG(file_stats.st_mode):
		# Regular files are green
		type_color = bcolors.OKGREEN
		size = byte_to(file_stats.st_size, 1)
	else:
		# Non-regular files are yellow, with sizes hidden
		type_color = bcolors.WARNING
		size = ''

	format_keywords = {
		'type_color': type_color,
		'name': fname,
		'colored_name': type_color + fname + bcolors.ENDC,
		'size': size,
		'size_color': size_color(file_stats.st_size),
		'atime': datetime.fromtimestamp(file_stats.st_atime),
		'ctime': datetime.fromtimestamp(file_stats.st_ctime),
		'mtime': datetime.fromtimestamp(file_stats.st_mtime),
	}

	# Add all colors to the format dictionary
	format_keywords.update({key: val for key, val in bcolors.__dict__.items() if not key.startswith('_')})

	print(format_string.format(**format_keywords), **print_keywords)


def print_files(format_string, **print_keywords):
	for fname in FILES:
		print_file(format_string, fname, **print_keywords)


args = []
validargs = set(('a', 'c', 'h', 'f', 's=l', 's=s', 'd'))
dtl = "."
for arg in sys.argv[1:]:
	if arg.startswith("-"):
		if arg[1:] in validargs:
			args.extend([arg])
		else:
			print("Invalid argument: " + arg, file=sys.stderr)
			exit(1)
	elif os.path.isdir(arg):
		dtl = arg
	else:
		print("Not a directory: " + arg, file=sys.stderr)
		exit(1)

if not '-c' in args and not '-f' in args:
	args.extend(['-d'])

os.chdir(dtl)
FILES = os.listdir()

if '-a' not in args:
	# Remove dotfiles from listing if we aren't showing all files
	FILES = [file for file in FILES if not file.startswith('.')]

for arg in args:
	if arg == "-h":
		help()
	elif arg.startswith("-s="):
		files_with_size = [(os.path.getsize(file), file) for file in FILES]
		# Sort files by size, reverse order if we're using "-s=l" (sort=largest first)
		files_with_size.sort(key=operator.itemgetter(0), reverse=arg == '-s=l')
		FILES = [file for size, file in files_with_size]

	elif arg == "-c":
		print_files('{colored_name}', end='  ')
		print()  # Ensure output ends in a newline
		exit();

	elif arg == "-d":
		print_files('{size_color}{size:8}{GRAY}| {colored_name}')
		exit();

	elif arg == "-f":
		print_files('{CYAN}{mtime:%c}{ENDC} {size_color}{size:8}{GRAY}| {colored_name}')
		exit();
