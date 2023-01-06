#Use a Debugger
#def mutate(a_list):
#  b_list = []
#  for item in a_list:
#    new_item = item * 2
#  b_list.append(new_item)
#  print(b_list)

#mutate([1,2,3,5,8,13])

#The error in the code shows that line 6 above is not indented inside the for loop which is the resason for p[rinting only one iten in the list.

def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
