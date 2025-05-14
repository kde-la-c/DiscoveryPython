#!/usr/bin/env python3

def get_int(msg):
	while True:
		try:
			var = int(input(msg))
			break
		except:
			print("invalid format, enter an integer")
	return var

first = get_int("Give me the first number: ")
second = get_int("Give me the second number: ")
print("Thank you!")
print(f"{first} + {second} = {first+second}")
print(f"{first} - {second} = {first-second}")
print(f"{first} / {second} = {first/second}")
print(f"{first} * {second} = {first*second}")