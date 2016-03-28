#!/usr/bin/env python3
import os

# --- CUSTOMIZE THIS --- #

VERSION = "2.0"
AUTHOR = "hdev1"
PKG_NAME = "'a'"
INSTALL_COMMANDS = ['sudo rm -rf /usr/bin/a', 'sudo cp ./a.py /usr/bin/a']
INSTALL_PATH_ENABLED = False
INSTALL_PATH = "."

# --- FUNCS --- #
def CHANGE_INSTALL_PATH():
	os.system("clear")
	print('\n')
	print(colors.BOLD + "		Install directory" + colors.END)
	print(colors.BOLD + "		⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯" + colors.END)
	print("		The default install path is " + INSTALL_PATH)
	print("		Enter either nothing or a")
	print("		valid install path. ")
	print(colors.BOLD + "		⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺" + colors.END)
	action = input("""-> """)
	if not os.path.isdir(action):
		print(colors.RED + "[" + symbols.CROSS + "]" + colors.END + " Invalid directory! Press Enter to re-enter the path.")


# --- PROGRAM --- #
class colors:
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	END = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
class symbols:
	CHECKMARK = "✔"
	CROSS = "✕"
	WARNING = "⚠"

os.system("clear")

# FIRST SCREEN
print('\n')
print(colors.BOLD + "		Welcome to the " + PKG_NAME + " setup." + colors.END)
print(colors.BOLD + "		⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯" + colors.END)
print("		Version: " + VERSION)
print("		Author: " + AUTHOR)
print(colors.BOLD + "		⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺" + colors.END)
action = input("""[E]xit						[C]ontinue
-> """)
if action != "C" and action != "c":
	print(colors.RED + "[" + symbols.CROSS + "]" + colors.END + " Installation aborted!")
	exit()

os.system("clear")

# INSTALL
print('\n')
print(colors.BOLD + "			Installing..." + colors.END)
print(colors.BOLD + "		⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯" + colors.END)
print("""		Running install commands...""")
for command in INSTALL_COMMANDS:
    os.system(command)
print(colors.BOLD + "		⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺" + colors.END)

os.system("clear")
# FINISH
print('\n')
print(colors.BOLD + "		Installation finished!" + colors.END)
print(colors.BOLD + "		⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯" + colors.END)
print("""		You can now run a with, well the
		command 'a'!""")
for command in INSTALL_COMMANDS:
    os.system(command)
print(colors.BOLD + "		⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺" + colors.END)


