#!/usr/bin/env python3

# def get_int(msg, err):
# 	while True:
# 		try:
# 			var = int(input(msg))
# 			if var < 0:
# 				raise
# 			break
# 		except:
# 			print(err)
# 	return var

# i = get_int(
# 	"Enter a number\n",
# 	"wrong format"
# )

# for j in range(10):
# 	k = j * i
# 	print(f"{j} x {i} = {k}")


try:
	i = int(input("Enter a number\n"))
	for j in range(10):
		k = j * i
		print(f"{j} x {i} = {k}")
except:
	print("invalid format, enter an integer")
