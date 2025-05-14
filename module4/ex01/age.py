#!/usr/bin/env python3

try:
	age = int(input("Please tell me your age:"))
	print(f"You are currently {age} years old.")
	for item in range(3):
		print(f"in {item*10+10} years, you'll be {age+(item*10)+10} years old")
except:
	print("invalid number, enter an integer")