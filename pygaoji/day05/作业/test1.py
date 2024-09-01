'''
a+b+c = 1000
'''
import math
import time
from pygaoji.day02.FoodManagerSystem.Utils import use_time
@use_time
def func1():
    for a in range(0, 1001):
        for b in range(a+1, 1001):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print(a, b, c)
                print(a*b*c)
                break

func1()