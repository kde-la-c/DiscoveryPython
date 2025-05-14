#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
	print("none")
else:
	try:
		i = int(sys.argv[1])
		j = int(sys.argv[2])
	except:
		print("none")
	else:
		arr = []
		if i < j:
			for item in range(j - i + 1):
				arr.append(item + i)
		else:
			for item in range(i - j + 1):
				arr.append(item + j)
		print(arr)