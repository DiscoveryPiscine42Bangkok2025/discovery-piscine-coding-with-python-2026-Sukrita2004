#!/usr/bin/env python3

def add_one(num):
    num = num + 1
    print("Inside add_one:", num)

number = 65
print("Before calling add_one:", number)
add_one(number)
print("After calling add_one:", number)
