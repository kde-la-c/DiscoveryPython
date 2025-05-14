#!/usr/bin/env python3

try:
	i = int(input("Enter a number\n"))
	for j in range(10):
		k = j * i
		print(f"{j} x {i} = {k}")
except:
	print("invalid format, enter an integer")
