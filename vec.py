from math import *

class Vec:

    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vec(self.x+other.x,self.y+other.y)
    
    def __sub__(self,other):
        return Vec(self.x-other.x,self.y-other.y)
    
    def __mul__(self,other):
        if(type(other.__name__)=='Vec'):
            return self.x*other.x+self.y*other.y
        else:
            return Vec(self.x*other,self.y*other)
        
    def __div__(self,other):
        return Vec(self.x/other,self.y/other)
    
    @property
    def length(self):
        return hypot(self.x,self.y)

    def add(self,v):
        result = Vec()
        result.x = self.x+v.x
        result.y = self.y+v.y
        return result
    
    def mul(self,k):
        result = Vec()
        result.x = k*self.x
        result.y = k*self.y
        return result
    
    def div(self,k):
        result = Vec()
        result.x = k*self.x
        result.y = k*self.y
        return result
    
    pass