# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 00:32:39 2020

@author: walte
"""

class Line():
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x1-x2)**2 + (y1-y2)**2)**0.5
    
    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y1-y2) / (x1-x2)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)
li.distance()
li.slope()

class Cylinder():
    pi = 3.14
    
    def __init__(self,height=1, radius=1):
        self.height = height
        self.radius = radius
    
    def volume(self):
        return Cylinder.pi*self.radius*self.radius*self.height
    
    def surface_area(self):
        return Cylinder.pi*2.0*self.radius*self.height + \
               Cylinder.pi*2.0*self.radius*self.radius

c = Cylinder(2,3)
c.volume()
c.surface_area()