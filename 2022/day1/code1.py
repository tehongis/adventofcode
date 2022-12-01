#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" https://adventofcode.com/2022/day/1 """

from pprint import pprint

f = open('input.txt','r')
data = f.readlines()
f.close()

tonttulist = []

tonttu=[]

for line in data:
    line=line.strip()
    if line == "":
        tonttulist.append(tonttu)
        tonttu=[]
    else:
        arvo = int(line)
        tonttu.append(arvo)

#pprint(tonttulist)

totalist= []

max = 0
for tonttu in tonttulist:
    total=0
    for value in tonttu:
        total = total + value
    totalist.append(total)
    if total > max:
        max = total
print(max)

totalist.sort()
pprint(totalist[-3:])
totaltotal=0
for value in totalist[-3:]:
    totaltotal=totaltotal+value
print(totaltotal)
