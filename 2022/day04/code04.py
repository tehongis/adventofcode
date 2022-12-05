#!/usr/bin/python3
# -*- coding: utf-8 -*-

from colorama import Fore, Back, Style


""" https://adventofcode.com/2022/day/4 """

import time
from pprint import pprint

f = open('input.txt','r')
data = f.readlines()
f.close()

def inrange(sections):
    section1,section2 = sections.split(',')
    a,b = section1.split('-')
    c,d = section2.split('-')

    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)

    if a == c and b == d:
        print(Fore.YELLOW,sections,"range",a,b,"is",c,d)
        return True

    if a >= c and b <=d:
        print(Fore.RED,sections,"range",c,d,"contains",a,b)
        return True

    if c >= a and d <=b:
        print(Fore.GREEN,sections,"range",a,b,"contains",c,d)
        return True

    print(Fore.BLUE,sections,a,b,c,d)
    return False

# part 2

def overlaps(sections):
    section1,section2 = sections.split(',')
    a,b = section1.split('-')
    c,d = section2.split('-')

    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)

    if a > c:
        a, b , c, d = c, d, a ,b

    if b >= c:
        print(Fore.CYAN,sections,"range",a,b,"overlaps",c,d)
        return True
    print(Fore.BLUE,sections,a,b,c,d)
    return False

sum1 = 0
for rivi in data:
    rivi=rivi.strip()
    if inrange(rivi):
        sum1 += 1
print(sum1)

sum2 = 0
for rivi in data:
    rivi=rivi.strip()
    if overlaps(rivi):
        sum2 += 1
print(sum2)
