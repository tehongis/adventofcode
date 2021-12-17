"""
The probe's x,y position starts at 0,0. Then, it will follow some trajectory by moving in steps. On each step, these changes occur in the following order:

The probe's x position increases by its x velocity.
The probe's y position increases by its y velocity.
Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
Due to gravity, the probe's y velocity decreases by 1.
"""

import time

class object:

    def __init__(self,x,y):
        self.x_pos = 0
        self.y_pos = 0
        self.x_vel = x
        self.y_vel = y

    def move(self):
        self.x_pos =self.x_pos + self.x_vel
        self.y_pos =self.y_pos + self.y_vel
        if self.x_vel > 0:
            self.x_vel = self.x_vel - 1
        if self.x_vel < 0:
            self.x_vel = self.x_vel + 1
        self.y_vel = self.y_vel - 1
        return(self.x_pos,self.y_pos)

    def check(self,area):
        xa = area[0][0]
        xb = area[0][1]
        ya = area[1][0]
        yb = area[1][1]
        if self.x_pos >= xa and self.x_pos <= xb and  self.y_pos >= ya and self.y_pos <= yb:
            return True
        return False

f = open('input.txt')
input = f.read().strip()
f.close

area_x,area_y = input[input.find(':')+1:].split(',')
xa,xb=area_x.strip().split('..')
ya,yb=area_y.strip().split('..')
xa=xa.split('x=')[1]
ya=ya.split('y=')[1]
area_x=[int(xa),int(xb)]
area_y=[int(ya),int(yb)]

area = [area_x,area_y]
print(area)


count = 0
for xvel in range(-300,300):
    for yvel in range(-300,300):
        probe = object(xvel,yvel)
        maxy = 0
        while probe.x_pos < area[0][1] and probe.y_pos > area[1][0]:
            x,y = probe.move()
            if y > maxy:
                maxy = y
            if probe.check(area):
                print(x,y,xvel,yvel,maxy ) 
                count += 1
print(count)
