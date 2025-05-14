#!/usr/bin/env python3

try:
	f = float(input("Give me a number: "))
	print(round(f + 0.5))
except:
	print("invalid format, enter an integer or decimal")