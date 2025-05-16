#!/usr/bin/env python3

def find_the_redheads(family):
	key, value = family
	return value == "red"

dupont_family = {
	"florian": "red",
	"marie": "blond",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
}
print(list(dict(filter(find_the_redheads, dupont_family.items())).keys()))