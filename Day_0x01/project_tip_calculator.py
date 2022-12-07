#!/usr/bin/env/python3

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

people = int(input("how many people to split the bill?"))

bill_tip = (tip / 100 + 1) * bill 

bill_person = bill_tip / people

payment = "{:.2f}".format(bill_person)

print(f"Each person should pay {payment} dollar")
