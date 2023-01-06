#for number in range(1, 101):
#  if number % 3 == 0 or number % 5 == 0:
#    print("FizzBuzz")
#  if number % 3 == 0:
#    print("Fizz")
#  if number % 5 == 0:
#    print("Buzz")
#  else:
#    print([number])


#Solution:
#The program above should be with an 'and' logic and not or because we are bringing the 2 codes together to output. The ifs statement under the first if statement should be elif as in else if.

for number in range(1, 101):
  if (number % 3 == 0) and (number % 5 == 0):
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print([number])
