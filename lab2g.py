#!/usr/bin/env python3
#Author: Marc Esmer Palaypay
#Author ID: mepalaypay1
#Date Created: 05/22/2026

import sys

arguments = sys.argv

if len(sys.argv) == 1:
	timer=3
else:
	timer = int(sys.argv[1])
	
while timer !=0:
	print(timer)
	timer = timer -1
print('blast off!')
