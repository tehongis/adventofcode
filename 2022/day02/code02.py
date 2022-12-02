#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" https://adventofcode.com/2022/day/1 """

import time
from pprint import pprint

"""
A for Rock
B for Paper
C for Scissors

X for Rock
Y for Paper
Z for Scissors

The winner of the whole tournament is the player with the highest score.
Your total score is the sum of your scores for each round.
The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round 
(0 if you lost, 3 if the round was a draw, and 6 if you won).
"""

scores = {
    'AX':1+3,
    'AY':1+6,
    'AZ':1+0,
    'BX':2+0,
    'BY':2+3,
    'BZ':2+6,
    'CX':3+6,
    'CY':3+0,
    'CZ':3+3
}

from pprint import pprint

f = open('input.txt','r')
data = f.readlines()
f.close()

totalscore = 0
for line in data:
    line=line.strip()
    game=line[0]+line[2]
    score=scores[game]
    totalscore=totalscore+score
print(totalscore)
    
# 13099 too low