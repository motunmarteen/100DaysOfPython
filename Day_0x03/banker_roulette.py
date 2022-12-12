#!/usr/bin/env/python3

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
banker_roulette = random.randint(0, 6)

if banker_roulette == 0:
    print(f"{names[0]} is going to buy the meal today!")

elif banker_roulette == 1:
    print(f"{names[1]} is going to buy the meal today!")

elif banker_roulette == 2:
    print(f"{names[2]} is going to buy the meal today!")

elif banker_roulette == 3:
    print(f"{names[3]} is going to buy the meal today!")

elif banker_roulette == 4:
    print(f"{names[4]} is going to buy the meal today!")

elif banker_roulette == 5:
    print(f"{names[5]} is going to buy the meal today!")

else:
    print(f"{names[6]} is going to buy the meal today!")
