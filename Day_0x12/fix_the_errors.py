# Fix the Errors
#age = input("How old are you?")
#if age > 18:
#print("You can drive at age {age}.")

#Indentation with print functio
#F-string not identified in the print function
#age is not converted to integer to be used in the comparison for the if statement

age = int(input("How old are you?: "))
if age > 18:
    print(f"You can drive at age {age}.")
