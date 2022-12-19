#!/usr/bin/env/python3

list_of_numbers = input("type in numbers of need: ").split()

max_number = list_of_numbers[0]
for n in list_of_numbers:
	if (n > max_number):
		max_number = n
print("maximum number is:", n)
