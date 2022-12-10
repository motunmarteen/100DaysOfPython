#!/usr/bin/env/python3

leap_year = int(input("What year do you want to check as leap year? "))

if leap_year % 4 == 0:
	if leap_year % 100 == 0:
		if leap_year == 0:
			print("This is a leap year.")
		else:
			print("This is not a leap year.")
	else:
		print("This is a leap year.")
else:
	print("This is not a leap year.")
