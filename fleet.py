from math import *
from vec import *

class Craft:
    k = 1.0#阻力系数

    def __init__(self,name,mass,power,x,y):
        self.name = name
        self.m = mass
        self.P = power
        #运动学参数
        self.pos = Vec(x,y)
        self.angle = pi/2
        self.v = Vec()
        self.a = Vec()
        #动力学参数
        self.F = Vec()
        self.f = Vec()

    def __str__(self):
        return 'Craft Object (name: %s,mass: %s,power: %s)' % (self.name,self.m,self.P)

    __repr__ = __str__

    def Update(self):
        #动力学计算
        if(self.v.length!=0):
            force = self.P/self.v.length
        else:
            force = 1.0
        self.F = Vec(force*cos(self.angle),force*sin(self.angle))
        self.f = self.v*(-k)
        self.a = (self.F+self.f)/self.m
        #运动学计算
        self.v = self.v+self.a
        self.pos = self.pos+self.v

    pass