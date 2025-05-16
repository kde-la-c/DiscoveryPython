#!/usr/bin/env python3
import sys

def downcase_it(string):
	return string.lower()

if len(sys.argv) < 2:
	print("none")
else:
	for i, item in enumerate(sys.argv):
		if i:
			print(downcase_it(item))