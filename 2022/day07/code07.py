#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" https://adventofcode.com/2022/day/6 """

import time
import os

from pprint import pprint

f = open('input.txt','r')
data = f.readlines()
f.close()

#$ cd stcfmz
#$ ls
#115637 lcgv

linecount=0


def nextLine():
    global linecount
    if linecount > len(data):
        return ""
    line=data[linecount]
    if len(line) == 0:
        return (line)
    linecount += 1 
    return line.strip()


def getFiles():
    global linecount
    output = []
    while True:
        line = nextLine()
        if line[0] == '$':
            linecount -= 1
            return output
        output.append(line)


filesystem = []
while linecount < len(data):
    line = nextLine()
    if len(line) == 0:
        break
    if line[0] == '$':
        command = line[2:]
        if command[0:2] == 'ls':
            print(command)
            result = getFiles()
            for line in result:
                print(line)

        if command[0:2] == 'cd':
            target = command[command.find(' ')+1:]
            if target == '..':
                print('cd up')
            else:
                print('cd to:', target)

#    if linecount > 20:
#        break


#    line=line.strip()
#    if line[0]=='$':
#        parsecommand(line)   
