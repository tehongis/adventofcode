#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" https://adventofcode.com/2022/day/1 """

import time
from pprint import pprint

f = open('input.txt','r')
data = f.readlines()
f.close()

sum = 0
for rivi in data:
    rivi=rivi.strip()
#    print(rivi)
    eka=rivi[:int(len(rivi) / 2)]
    toka=rivi[int(len(rivi) / 2):]
    print(eka, toka)
    arvo = 0
    for merkki in eka:
        if merkki in toka:
            #A=65   Z=90
            #a=97   z=122
            arvo = ord(merkki)
            if arvo >=65 and arvo <=90:
                arvo = arvo - 65 + 27
            if arvo >=97 and arvo <=122:
                arvo = arvo - 96
            #if arvo
            print(merkki,arvo)
            break
    sum = sum + arvo
print(sum)