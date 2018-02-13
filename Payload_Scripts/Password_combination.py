import os
import re
import sys
from itertools import permutations

continue_string = True

# Provide the strings of your own or scrape from the application. Scripts provides the combination of all strings as a password which can be used for password bruteforce.

def function1():
	string_data = raw_input("Enter the possible strings: ")
	split_data = re.findall(r'\S+', string_data)
	filepath = os.path.join(os.getcwd(),'Password_output.txt')
	perms = [''.join(p) for p in permutations(split_data)]
	f = open(filepath, 'a')
	for a in perms:
		d = a.rstrip()
		f.write(d)
		f.write("\n")
	f.close()

function1()

# Will prompt the user to continue or abort the process

while continue_string:
	new_data = raw_input("Would you like to continue with more strings (y/n)...??")
	if new_data == "y" or new_data == "Y":
		function1()
	elif new_data == "n" or new_data == "N":
		continue_string = False
	else:
		break