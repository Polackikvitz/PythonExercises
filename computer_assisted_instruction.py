#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:23:21 2024

@author: calvinberndt
"""
import random


def number_generator(difficulty):
    '''Returns a tuple with two random numbers 1-10'''
    if difficulty == 1:
        int1 = random.randrange(1, 11)
        int2 = random.randrange(1, 11)
        digits = (int1, int2)  # packing tuple
    elif difficulty == 2:
        int1 = random.randrange(1, 100)
        int2 = random.randrange(1, 100)
        digits = (int1, int2)  # packing tuple
    else:
        print('You did not type 1 or 2.')
    return digits


def operation(operator, int1, int2):
    symbol = ['+', '-', '*', '/']
    symbol = symbol[operator - 1]
    if operator == 1:
        key = int1 + int2
        answer = int(input(f'How much is {int1} {symbol} {int2}? '))
    elif operator == 2:
        key = int1 - int2
        answer = int(input(f'How much is {int1} {symbol} {int2}? '))
    elif operator == 3:
        key = int1 * int2
        answer = int(input(f'How much is {int1} {symbol} {int2}? '))
    elif operator == 4:
        key = int1 / int2
        answer = int(input(f'How much is {int1} {symbol} {int2}? '))
    key_and_response = (key, answer, symbol)
    return key_and_response


def responses():
    '''Returns a random response'''
    correct = ['Good job!', 'Keep up the good work', 'Very good']
    incorrect = ['Incorrect', 'Better luck next time', 'Please try again.']
    correct_index = random.randrange(0, len(correct))
    incorrect_index = random.randrange(0, len(incorrect))
    response = correct[correct_index], incorrect[incorrect_index]
    return response


def ask_question():
    '''Prompts user with multiplication question'''
    difficulty = int(input('Please enter 1 for level 1 or 2 for level 2: '))
    # calling function and unpacking tuple
    int1, int2 = number_generator(difficulty)
    operator = int(input(
        '1 for addition. 2 for subtration. 3 for multiplication. 4 for division. '))
    key, answer, symbol = operation(operator, int1, int2)
    correct, incorrect = responses()  # calling function and unpacking tuple

    while key != answer:
        correct, incorrect = responses()  # calling function and unpacking tuple
        print(incorrect)
        answer = int(input(f'How much is {int1} {symbol} {int2}? '))
    print(correct)


ask_question()
