import random
import sys

number_of_dice = int(sys.argv[1])
min = 1
max = 6

while number_of_dice >0:
    roll = random.randint(min,max)
    print(roll)
    number_of_dice = number_of_dice - 1

    
