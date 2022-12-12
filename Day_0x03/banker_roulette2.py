#!/usr/bin/env/python3

import random

names_input = input("Type in the names seperating them with comma and space: ")
names = names_input.split(", ")
lenght_names = len(names)
random_number = random.randint(0, lenght_names -1)
random_name = names[random_number]
print(f"{random_name} will pay for the meal")
