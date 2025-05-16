#!/usr/bin/env python3

def greetings(name = "noble stranger"):
	try:
		if all(x.isalpha() or x.isspace() for x in name):
			print("Hello,", name)
	except:
		print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)