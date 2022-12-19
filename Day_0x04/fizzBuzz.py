#!/usr/bin/python3

for number in range(1, 101):
	if number % 3 == 0 and number % 5 == 0:
		print(f"FizzBuzz")
	elif number % 5 == 0:
		print(f"Buzz")
	elif number % 3 == 0:
		print(f"Fizz")
	else:
		print(f"{number}")
