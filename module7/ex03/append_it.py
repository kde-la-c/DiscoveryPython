#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
	print("none")
else:
	for i, item in enumerate(sys.argv):
		if not item.endswith("ism") and i:
			print(item + "ism")