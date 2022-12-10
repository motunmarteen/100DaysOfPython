#!/usr/bin/env/python3

height = float(input("What is your height in m: "))
weight = float(input("What is your weight in kg: "))

bmi = round(weight / (height ** 2))

if bmi < 18.5:
	print(f"You are underweight because your bmi is {bmi}")
elif bmi < 25:
	print(f"You have a normal weight because your bmi is {bmi}")
elif bmi < 30:
	print(f"You are overweight because your bmi is {bmi}")
elif bmi <  35:
	print(f"You are obese because your bmi is {bmi}")
else:
	print(f"You are clinically obese because your bmi is {bmi}.")
