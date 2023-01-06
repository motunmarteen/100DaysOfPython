#Debug the program below

#number = int(input("Which number do you want to check?: "))

#if number % 2 = 0:
 #   print("This is an even number.")
#else:
#    print("This is an odd number.")


#Solution:
#To solve this, we have to identify that the if statement is carrying an equal to sign and not an assignmnet sign which compare a statement, hence there will not be a value to check.

number = int(input("Which number do you want to check?: "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

