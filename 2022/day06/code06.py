#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" https://adventofcode.com/2022/day/6 """

import time
import os

from pprint import pprint

f = open('input.txt','r')
data = f.readlines()
f.close()

jono = "                       "
checksize = 4
#checksize = 14 part 2

def checkBuffer(jono):
    char_set = [False] * 128
    for c in jono:
        val = ord(c)
        if char_set[val]:
            return False
        char_set[val] = True
    return True

count = 0
for row in data:
    for merkki in row:
        if merkki == "\n":
            break
        jono = jono[1:checksize] +merkki
        count += 1
        if count >= checksize:
            if checkBuffer(jono):
                print(jono,count)
                break
