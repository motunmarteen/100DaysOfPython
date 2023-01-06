#year = input("Which year do you want to check?")

#if year % 4 == 0:
#  if year % 100 == 0:
#    if year % 400 == 0:
#      print("Leap year.")
#    else:
#      print("Not leap year.")
#  else:
#    print("Leap year.")
#else:
#  print("Not leap year.")

#The code above has to recive a number as the input, however, the number received will have to be coverted to integer using the int() converter in line one of the code so tha the line of code which is line 1 will have to be compared to the value of integer it will be modulo to.



year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
