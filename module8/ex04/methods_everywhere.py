#!/usr/bin/env python3
import sys

def shrink(string):
	return(string[0:8])

def enlarge(string):
	return((string + "ZZZZZZZZ"[0:8 - len(string)]))

for i, item in enumerate(sys.argv):
	if i:
		if len(item) > 8:
			print(shrink(item))
		elif len(item) < 8:
			print(enlarge(item))
		else:
			print(item)