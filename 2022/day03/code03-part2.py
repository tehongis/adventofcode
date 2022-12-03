#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" https://adventofcode.com/2022/day/1 """

import time
from pprint import pprint

f = open('input.txt','r')
data = f.readlines()
f.close()

def merkki2prio(merkki):
    #A=65<->Z=90 a=97<->z=122
    arvo = ord(merkki)
    if arvo >=65 and arvo <=90:
        arvo = arvo - 65 + 27
    if arvo >=97 and arvo <=122:
        arvo = arvo - 96
    return arvo


sum = 0
for bag1,bag2,bag3 in zip(*[iter(data)]*3):
    bag1=bag1.strip()
    bag2=bag2.strip()
    bag3=bag3.strip()
    print(bag1,bag2,bag3)
    for merkki in bag1:
        if merkki in bag2 and merkki in bag3:
            print(merkki)
            sum = sum + merkki2prio(merkki)
            break

print(sum)
