# import random
from random import randint, seed
# seed(1)
# print(randint(0, 1))
num = randint(0, 1)

if num == 0:
    print('HEAD!')
else:
    print('TAILS!')
