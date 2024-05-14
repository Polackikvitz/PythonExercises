#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 18:05:41 2024

@author: calvinberndt
"""

import random
import sys

start = input('To start the game type "yes" and to quit type "no": ')
if start.lower() == 'no':
    sys.exit()
else:
    print("Let's play this game of craps!")

instructions = input("Welcome to the game of chance. Are you ready to test your fortune on the game of craps? Type yes if you need further instructions or no if you want to continue to the game!")   
if instructions == 'yes':
    print(''' 1. player rolls two six-sided dice and adds the numbers rolled together.
              2. On this first roll, a 7 or an 11 automatically wins, and a 2, 3, or 12automatically loses, and play is over.
                 If a 4, 5, 6, 8, 9, or 10 are rolled on this first roll, that number becomes the 'point.'
              3. The player continues to roll the two dice again until one of two things happens: 
                 either they roll the 'point' again, in which case they win; or they roll a 7, in which case they lose.''')
if instructions == 'yes':
    ready = input('Are you ready to rumble! Type yes if you are: ')

if ready != 'yes':
    sys.exit()


def roll_die():
    """Roll two dice and return their face values as a tuple"""
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    return (die1, die2) #packing a tuple

def display_dice(dice):
    dice1, dice2 = dice #unpacking tuple
    print(f'Player rolled {dice1} + {dice2} = {sum(dice)}')



die_values = roll_die()
display_dice(die_values)

sum_of_dies = sum(die_values)
 
if sum_of_dies in (7,11):
    game_status = 'WIN'
    print('You won the game of craps!')

elif sum_of_dies in (2, 3, 12):
    game_status = 'LOST'
    print('You lost the game of craps!')

else: 
    game_status = 'CONTINUE'
    my_point = sum_of_dies
    print(f'My point is {my_point}')

while game_status == 'CONTINUE':
    die_values = roll_die()
    display_dice(die_values)
    sum_of_dies = sum(die_values)
    if sum_of_dies == my_point:
        game_status = 'WIN'
        print('You won the game of craps!')

    elif sum_of_dies == 7:
        game_status = 'LOST'
        print('You lost the game of craps!')
    