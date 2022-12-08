#!/usr/bin/env/python3

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / height ** 2)

if bmi <= 18:
    print("Your BMI is " + str(bmi) + ", " + "you are underweight.")
elif bmi <= 22:
    print("Your BMI is " + str(bmi) + ", " + "you have a normal weight.")
elif bmi <= 28:
    print("Your BMI is " + str(bmi) + ", " + "you are slightly overweight.")
elif bmi <= 33:
    print("Your BMI is " + str(bmi) + ", " + "you are obese.")
elif bmi >= 35:
    print("Your BMI is " + str(bmi) + ", " + "you are clinically obese.")
else:
    print("Nothing")
