#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 2:
	print("none")
else:
	arr = re.findall("z", sys.argv[1])
	if not arr:
		print("none", end="")
	for item in arr:
		print(item, end="")
	print()