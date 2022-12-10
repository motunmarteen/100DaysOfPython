#!/usr/bin/env/python3

height = int(input("What is your height? "))
bill = 0

if height >= 120:

	print("You are welcome on board for the Rollercoaster experince")
	
	age = int(input("How old are you? "))

	if age <= 18:
		bill = 5
		print("you are paying $5")

	elif age <= 40:
		bill = 7
		print("You are paying $7")

	else:
		bill = 10
		print("You are paying $10")
	
	picture = input("Hey, hold on!, would you love to take some pictures? Y or N\n")
	picture_cost = bill + 3

	if picture == "Y":
		print(f"Thank you, your total bill is ${picture_cost}, have a great ride.")
	else:
		print(f"Thank you, your total bill remains ${bill}, have a great ride.")
else:
	print("Sorry, you have to grow taller to be on the Rollercoaster")
