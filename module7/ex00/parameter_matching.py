#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
	print("none")
else:
	ret = input("What was the parameter? ") == sys.argv[1]
	if ret:
		print("Good Job!")
	else:
		print("Nope, sorry...")