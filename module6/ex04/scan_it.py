#!/usr/bin/env python3
import re
import sys

if not len(sys.argv) == 3:
	print("none")
else:
	nbrep = len(re.findall(sys.argv[1], sys.argv[2]))
	if nbrep:
		print(nbrep)
	else:
		print("none")