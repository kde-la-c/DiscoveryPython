#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
arr2 = set()
for item in arr:
	if item > 5:
		arr2.add(item + 2)
print(arr)
print(arr2)