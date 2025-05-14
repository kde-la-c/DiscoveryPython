#!/usr/bin/env python3

inp = input("give me a number: ")
try:
	f = float(inp)
	if f.is_integer():
	 	print("This number is an integer.")
	else:
		print("This number is a decimal.")
except:
	print("This is not a number.")
