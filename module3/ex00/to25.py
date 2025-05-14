#!/usr/bin/env python3

try:
	i = int(input("Enter a number less than 25\n"))
	if i > 25:
		print("Error")
	else:
		while i <= 25:
			print(f"Inside the loop, my variable is {i}")
			i += 1
except:
	print("invalid format, enter an integer")
