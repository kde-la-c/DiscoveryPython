#!/usr/bin/env python3
import sys

if len(sys.argv) < 3:
	print("none")
else:
	for i, arg in enumerate(reversed(sys.argv)):
		if not i == len(sys.argv) - 1:
			print(arg)