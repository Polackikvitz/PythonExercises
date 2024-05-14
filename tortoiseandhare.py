#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:57:59 2024

@author: calvinberndt
"""
import random


def tortoise():
    '''Moves the tortoise'''
    number = random.randrange(1, 11)
    if number < 6:
        return 3
    elif number in (6, 7):
        return -6
    else:
        return 1


def hare():
    '''Moves the hare'''
    number = random.randrange(1, 11)
    if number in (1, 2):
        return 0
    elif number in (3, 4):
        return 9
    elif number == 5:
        return -12
    elif number in (6, 7, 8):
        return 1
    else:
        return -2


def display(tort, hare):
    '''Displays the race'''
    tort_position = tort - 1  # minus 1 allow for position of T and zero index
    hare_position = hare - 1

    race_track = ' ' * 80
    race_track_list = list(race_track)

    if tort_position == hare_position:
        race_track_list[tort_position] = 'OUCH!'

    else:
        race_track_list[tort_position] = 'T'
        race_track_list[hare_position] = 'H'

    updated_race_track = ''.join(race_track_list)
    print(updated_race_track)


def race():
    '''Inner components of the race'''
    timer = 0
    tort_position = 1
    hare_position = 1
    print('BANG!! \n AND THEY ARE OFF!')
    while tort_position < 71 and hare_position < 71:
        timer += 1
        tort_position += tortoise()
        hare_position += hare()

        if tort_position < 1:
            tort_position = 1

        if hare_position < 1:
            hare_position = 1

        display(tort_position, hare_position)
        if tort_position > hare_position:
            input(f'{timer} seconds. Tortoise is winning! Press Enter.')
        elif hare_position > tort_position:
            input(f'{timer} seconds. Hare is winning! Press Enter.')
        else:
            input(f'{timer} seconds. A tie! The hare just bit the tort! Press Enter.')
    if tort_position > 70:
        print('TORTOISE WINS! YAY!!')
    if hare_position > 70:
        print('Hare wins. Yuck.')


race()
