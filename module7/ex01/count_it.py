#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
	print("none")
else:
	print("parameters:", len(sys.argv) - 1)
	for i, arg in enumerate(sys.argv):
		if not i == 0:
			print(arg + ":", len(arg))
