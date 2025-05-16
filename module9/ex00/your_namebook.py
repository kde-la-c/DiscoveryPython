#!/usr/bin/env python3

def array_of_names(names):
	arr = []
	for x, y in names.items():
		arr.append(f"{x.capitalize()} {y.capitalize()}")
	return arr

names = {
	"jean": "valjean",
	"kevin": "de la colina",
	"fifi": "brindacier"
}
print(array_of_names(names))