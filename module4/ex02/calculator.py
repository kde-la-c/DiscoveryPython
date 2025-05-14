#!/usr/bin/env python3

try:
	first = int(input("Give me the first number: "))
	second = int(input("Give me the second number: "))
	print("Thank you!")
	print(f"{first} + {second} = {first+second}")
	print(f"{first} - {second} = {first-second}")
	try:
		print(f"{first} / {second} = {first/second}")
	except:
		print(f"{first} / {second} = invalid division")
	print(f"{first} * {second} = {first*second}")
except:
	print("invalid format, enter an integer")
