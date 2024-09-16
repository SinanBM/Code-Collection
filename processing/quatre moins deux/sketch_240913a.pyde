#import random integer modul from random modul
from random import randint

# create a window by 500*500
def setup():
    size(500,500)
    background(255)
    
def draw():
    pass
    
def keyPressed():
    
    if key == "0":
        background(255)
        
    if key == "1":
        stroke(204, 102, 0)
        for i in range(0,10):
            for j in range(0,10):
                r = randint(1,6)
                if r == 1:
                    line(5+17*i,5+17*j,5+17*i,15+17*j)
                    line(5+17*i,15+17*j,15+17*i,15+17*j)
                if r == 2:
                    line(5+17*i,5+17*j,5+17*i,15+17*j)
                    line(5+17*i,5+17*j,15+17*i,5+17*j)
                if r == 3:
                    line(15+17*i,5+17*j,15+17*i,15+17*j)
                    line(5+17*i,15+17*j,15+17*i,15+17*j)
                if r == 4:
                    line(5+17*i,5+17*j,5+17*i,15+17*j)
                    line(15+17*i,5+17*j,15+17*i,15+17*j)
                if r == 5:
                    line(5+17*i,5+17*j,15+17*i,5+17*j)
                    line(5+17*i,15+17*j,15+17*i,15+17*j)
                if r == 6:
                    line(5+17*i,5+17*j,15+17*i,5+17*j)
                    line(15+17*i,5+17*j,15+17*i,15+17*j)
    
        
       
