# Reproduce the Bug

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

#This code will no run becuase the randint concept accepts the first number and the last number in it randomisation. While the list above starts from 0 to 5, the ranomisation when 6 is randomly selected will be out of index. So therefore, we will need to reassign the index to the randoms.

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
