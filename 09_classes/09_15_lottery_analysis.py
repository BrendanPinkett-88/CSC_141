# lottery analysis

from random import choice


lottery_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                   'A', 'B', 'C', 'D', 'E']


my_ticket = [1, 5, 'A', 'C']

attempts = 0

while True:
    pulled_numbers = []

    for number in range(4):
        pulled_numbers.append(choice(lottery_numbers))

    attempts += 1