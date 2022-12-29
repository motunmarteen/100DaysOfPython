import random

first_name = input("Type in your First Name\n").lower()
surname = input("Type in your Surname\n").lower()

len_first_name = int(len(first_name))
len_surname = int(len(surname))

random_first_name = random.randint(0, len_first_name - 1)
random_surname = random.randint(0, len_surname - 1)

first_name_surname = ((first_name[:random_first_name]) + (surname[random_surname:]))

print(first_name_surname)
