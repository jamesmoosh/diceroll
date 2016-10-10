## diceroll simulator
## 10/10/16 -jrkg

import random
import sys
if len(sys.argv) == 0:
    print("Please specify the number of dice to roll.")
    sys.ext(1)

number_of_dice = int(sys.argv[1])
min = 1
max = 6

print("The dice values are")
while number_of_dice >0:
    roll = random.randint(min,max)
    print(roll)
    number_of_dice = number_of_dice - 1

    
