#!/usr/bin/env python3
import re
import sys

if not len(sys.argv) == 3:
	print("none")
else:
	print(len(re.findall(sys.argv[1], sys.argv[2])))