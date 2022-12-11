#!/usr/bin/env/python3

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()

T1 = int(name1_lower.count('t'))
T2 = int(name2_lower.count('t'))

R1 = int(name1_lower.count('r'))
R2 = int(name2_lower.count('r'))

U1 = int(name1_lower.count('u'))
U2 = int(name2_lower.count('u'))

E1 = int(name1_lower.count('e'))
E2 = int(name2_lower.count('e'))

L1 = int(name1_lower.count('l'))
L2 = int(name2_lower.count('l'))

O1 = int(name1_lower.count('o'))
O2 = int(name2_lower.count('o'))

V1 = int(name1_lower.count('v'))
V2 = int(name2_lower.count('v'))

E1 = int(name1_lower.count('e'))
E2 = int(name2_lower.count('e'))

true = (T1 + T2 + R1 + R2 + U1 + U2 + E1 + E2) * 10
love = (L1 + L2 + O1 + O2 + V1 + V2 + E1 + E2)
true_love = true + love

if true_love < 10 or true_love > 90:
	print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 and true_love <= 50:
	print(f"Your score is {true_love}, you are alright togeher.")
else:
	print(f"Your score is {true_love}.")
