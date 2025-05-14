#!/usr/bin/env python3

def get_int(msg):
	while True:
		try:
			var = int(input(msg))
			if var < 0:
				raise
			break
		except:
			print("invalid number, enter an integer")
	return var

age = get_int("Please tell me your age:")
print(f"You are currently {age} years old.")
for item in range(3):
	print(f"in {item*10+10} years, you'll be {age+(item*10)+10} years old")