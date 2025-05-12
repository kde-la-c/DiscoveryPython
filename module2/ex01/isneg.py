#!/usr/bin/env python3

def get_int():

	while True:
		try:
			var = int(input())
			break
		except:
			print("invalid format, try again")
	return var

i = get_int()
if not i:
	print("This number is both positive and negative.")
elif i < 0:
	print("This number is negative.")
else:
	print("This number is positive.")
