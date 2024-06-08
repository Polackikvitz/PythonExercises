#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:55:43 2024

@author: calvinberndt

Poker Game Utilizing Lists and Tuples

"""

import random
from collections import Counter


def is_sequential(poker_Player):
    '''Checks for sequential card values'''

    # Unpack Tuple
    values = [value for face, suit, value in poker_Player]
    if 1 in values:
        values.append(14)

    # Sort List
    sorted_values = sorted(values)

    # Check if values are sequential
    for i in range(1, len(sorted_values)):

        if sorted_values[i] != sorted_values[i-1] + 1:
            return False

    return True


def return_highest_value(poker_Player):
    '''Checks Player and returns highest value (used for breaking ties)
        for flushes and straights'''

    # Unpack Tuple
    values = [value for face, suit, value in poker_Player]

    if 1 in values:
        values.append(14)

    # Sort List
    sorted_values = sorted(values)
    return sorted_values[-1]


def royal_flush(poker_Player):
    '''Checks Player values in comparison to Royal Flush values'''

    values = [value for face, suit, value in poker_Player]
    sorted_values = sorted(values)
    royal_flush_values = [1, 10, 11, 12, 13]

    if sorted_values == royal_flush_values:
        return True
    else:
        return False


def counter(value, count=[0]):
    '''Produces a counter, for player #, to maintain value while being called in function'''

    count[0] += value
    return count[0]


def Player_type(poker_Player):
    '''Displays Player-type'''

    count = counter(1)
    '''Determine the type of poker Player and return its score and highest values'''
    face_count = Counter(value for face, suit, value in poker_Player)
    suit_count = Counter(suit for face, suit, value in poker_Player)

    pairs = [value for value, count in face_count.items() if count == 2]
    threes = [value for value, count in face_count.items() if count == 3]
    fours = [value for value, count in face_count.items() if count == 4]
    flush = [count for count in suit_count.values() if count == 5]

    if len(flush) == 1 and royal_flush(poker_Player):
        print(f'Player {count} has: Royal Flush')
        return 1, 100, [], [], []

    elif is_sequential(poker_Player) and len(flush) == 1:
        print(f'Player {count} has: Straight Flush')
        return 2, return_highest_value(poker_Player), [], [], []

    elif len(fours) == 1:
        print(f'Player {count} has: Four of a Kind')
        return 3, return_highest_value(poker_Player), [], [], fours

    elif len(threes) == 1 and len(pairs) == 1:
        print(f'Player {count} has: Full House')
        return 4, return_highest_value(poker_Player), [], threes, pairs

    elif len(flush) == 1:
        print(f'Player {count} has: Flush')
        return 5, return_highest_value(poker_Player), [], [], []

    elif is_sequential(poker_Player):
        print(f'Player {count} has: Straight')
        return 6, return_highest_value(poker_Player), [], [], []

    elif len(threes) == 1:
        print(f'Player {count} has: Three of a Kind')
        return 7, return_highest_value(poker_Player), [], threes, []

    elif len(pairs) == 2:
        print(f'Player {count} has: Two Pair')
        return 8, return_highest_value(poker_Player), pairs, [], []

    elif len(pairs) == 1:
        print(f'Player {count} has: One Pair')
        return 9, return_highest_value(poker_Player), pairs, [], []

    else:
        print(f'Player {count} has: Nothing')
        return 10, return_highest_value(poker_Player), [], [], []


def initialize_deck():
    '''Set up the deck and poker Player'''

    # Define faces and suits
    faces = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
             'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    # Create list of tuples with a nested for loop.
    deck_of_cards = [(face, suit, (value + 1))
                     for suit in suits for value, face in enumerate(faces)]

    # Shuffle list
    random.shuffle(deck_of_cards)

    # Display list in four columns
    for i, card in enumerate(deck_of_cards):
        print(f'{card[0]} of {card[1]} Value: {card[2]:<20}', end='\t')
        if (i + 1) % 4 == 0:
            print()

    print()

    # Display 5-Card Poker Player using List Comprehension
    poker_Player1 = [card for i, card in enumerate(deck_of_cards) if i < 5]

    # Removes the cards that were just dealt
    deck_of_cards = deck_of_cards[5:]
    poker_Player2 = [card for i, card in enumerate(deck_of_cards) if i < 5]

    print()
    print('Player 1: ', poker_Player1)
    print()
    print('Player 2: ', poker_Player2)
    print()
    score1, highest_value1, pairs1, threes1, fours1 = Player_type(poker_Player1)
    score2, highest_value2, pairs2, threes2, fours2 = Player_type(poker_Player2)

    # Check which Player wins
    if score1 < score2:
        print('Player 1 wins!')
    elif score1 > score2:
        print('Player 2 wins!')
    else:  # Tie-breaking logic

        # Check for full house
        if pairs1 and pairs2 and threes1 and threes2:
            if max(threes1) > max(threes2):
                print(
                    f'Player 1 has a higher full house. Player 1:{max(threes1)}  >  Player 2:{max(threes2)}')
            elif max(threes1) < max(pairs2):
                print(
                    f'Player 2 has a higher full house. Player 1: {max(threes1)}  <  Player 2: {max(threes2)}')
            else:
                print('Tie!')

        # Check pair ties
        elif pairs1 and pairs2:
            if max(pairs1) > max(pairs2):
                print(
                    f'Player 1 has a higher pair. Player 1:{max(pairs1)}  >  Player 2:{max(pairs2)}')
            elif max(pairs1) < max(pairs2):
                print(
                    f'Player 2 has a higher pair. Player 1: {max(pairs1)}  <  Player 2: {max(pairs2)}')
            else:
                print('Tie!')

        elif threes1 and threes2:
            if max(threes1) > max(threes2):
                print(
                    f'Player 1 has a higher three of a kind. Player 1:{max(threes1)}  >  Player 2:{max(threes2)}')
            elif max(threes1) < max(pairs2):
                print(
                    f'Player 2 has a higher three of a kind. Player 1: {max(threes1)}  <  Player 2: {max(threes2)}')
            else:
                print('Tie!')

        elif fours1 and fours2:
            if max(fours1) > max(fours2):
                print(
                    f'Player 1 has a higher four of a kind. Player 1:{max(fours1)}  >  Player 2:{max(fours2)}')
            elif max(threes1) < max(pairs2):
                print(
                    f'Player 2 has a higher four of a kind. Player 1: {max(fours1)}  <  Player 2: {max(fours2)}')
            else:
                print('Tie!')

        # Straights, flushes, and nothing in Player
        elif highest_value1 > highest_value2:
            print('Player 1 wins by highest card!')

        elif highest_value1 < highest_value2:
            print('Player 2 wins by highest card!')

        else:
            print('However unlikely, a tie!')


initialize_deck()
