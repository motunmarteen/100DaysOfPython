#Calculator
#from art import logo
#Write function for all the operators and operands to be used in the calculaiton
#Add Function
def add(n1, n2):
  """This is a function to add numbers together"""
  return n1 + n2

#subtract Function
def subtract(n1, n2):
  """This is a function that subtracts numbers"""
  return n1 - n2

#Multiply Function
def multiply(n1, n2):
  """This is a function that multiplies numbers"""
  return n1 * n2

#Divide Function
def divide(n1, n2):
  """This is a function that divides numbers"""
  return n1 / n2

#Modulo Function
def modulo(n1, n2):
  """This is a function that checks for the remainder of operands fater they are divided"""
  return n1 % n2

def exponential(n1, n2):
  """This is a function that powers an operand in 2"""
  return n1 ** n2


#Then we create a dictionary called operations where the keys will be the symbols we have used above.

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              "%": modulo,
              "**": exponential
}


def calculator():
  #print(logo)
  #Derive a variable that accepts an input of operands to be used.
  num1 = float(input("What is the first number?: "))
  #Then we loop through the operations dictionary to pick out he symbols to be used
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    
    #Then we get hold of the calculation symbol
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()
calculator()
