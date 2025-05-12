#!/usr/bin/env python3

def get_int_positive(msg):
	while True:
		try:
			var = int(input(msg))
			if var < 0:
				raise
			break
		except:
			print("invalid number, enter a positive integer")
	return var

i = get_int_positive("Enter a number less than 25\n")

if i > 25:
    print("Error")
else:
    while i <= 25:
        print(f"Inside the loop, my variable is {i}")
        i += 1
	