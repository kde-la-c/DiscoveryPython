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
	print("This number is equal to zero.")
else:
	print("This number is different from zero")
