#!/usr/bin/env python3

num = input("give me a number: ")
try:
    number = float(num)
    try:
        number = int(num)
    except:
        print("This number is a decimal.")
    else:
        print("This number is an integer.")
except:
    print("This is not a number.")