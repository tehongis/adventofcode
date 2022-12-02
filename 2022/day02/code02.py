#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" https://adventofcode.com/2022/day/1 """

from pprint import pprint

f = open('input.txt','r')
data = f.readlines()
f.close()

for line in data:
    line=line.strip()
    player,me=line.split()
    print(player,me)
    
