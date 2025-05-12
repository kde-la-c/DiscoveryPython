#!/usr/bin/env python3

def get_int(msg):

	while True:
		try:
			var = int(input(msg))
			break
		except:
			print("invalid format, try again")
	return var

i = get_int("Enter the first number:\n")
j = get_int("Enter the second number:\n")
ret = i * j

print(f"{i} x {j} = {ret}")
if not ret:
	print("The result is both positive and negative.")
elif ret < 0:
	print("The result is negative.")
else:
	print("The result is positive.")
