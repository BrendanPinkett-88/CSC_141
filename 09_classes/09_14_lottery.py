# lottery

import random
import numbers

lottery_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                   'A', 'B', 'C', 'D', 'E']

list_of_random = random.sample(lottery_numbers, 1) + random.sample(lottery_numbers, 2)

lottery_ticket = random.sample(list_of_random, 3)
print("Your lottery ticket:", lottery_ticket)
