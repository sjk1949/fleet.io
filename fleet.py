from math import *
from vec import *

class Craft:
    k = 1000.0#阻力系数

    def __init__(self,name,mass,power,x,y):
        self.name = name
        self.m = mass
        self.Pmax = power
        self.P = 0.0
        #运动学参数
        self.pos = Vec(x,y)
        self.angle = 90.0
        self.v = Vec()
        self.a = Vec()
        #动力学参数
        self.startF = 2000.0#启动力
        self.F = Vec()
        self.f = Vec()
        #图形参数
        self.render = None

    def __str__(self):
        return 'Craft Object (name: %s,mass: %s,power: %s)' % (self.name,self.m,self.P)

    __repr__ = __str__

    def Update(self):
        #动力学计算
        if(self.P!=0):
            if(self.F.length*self.v.length>=self.Pmax):
                force = self.P/self.v.length
            else:
                force = self.startF
        else:
            force = 0.0
        self.F = Vec(force*cos(pi*self.angle/180),force*sin(pi*self.angle/180))
        self.f = self.v*(-Craft.k)
        self.a = (self.F+self.f)/self.m
        #运动学计算
        self.v = self.v+self.a
        self.pos = self.pos+self.v
        #print("v %lf %lf a %lf %lf F %lf %lf f %lf %lf P %lf" % (self.v.x,self.v.y,self.a.x,self.a.y,self.F.x,self.F.y,self.f.x,self.f.y,self.F.length*self.v.length))

    pass