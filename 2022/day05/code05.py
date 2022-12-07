#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" https://adventofcode.com/2022/day/1 """

import time
import os

from pprint import pprint

f = open('input.txt','r')
data = f.readlines()
f.close()


initialstate = data[0:9]
pprint(initialstate)
containers = []
for x in range(0,9):
    row = []
    for y in range(1,9):
        row.append(initialstate[8-y][1+x*4])
    #print(row)
    containers.append(row)
pprint(containers)    

check = False
for rivi in data:
    rivi=rivi.strip()
    if check:
        print(rivi)
        time.sleep(2)

    if len(rivi) == 0:
        check = True

