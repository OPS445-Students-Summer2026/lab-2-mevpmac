#!/usr/bin/env python3

import sys

arguments = sys.argv

if len(sys.argv) !=3:
	
	print('Usage: ' + sys.argv[0] + ' name age')
	sys.exit()

name = sys.argv[1]
age = sys.argv[2]

print('Hi ' + sys.argv[1] + ', you are ' + sys.argv[2] + ' years old.')
