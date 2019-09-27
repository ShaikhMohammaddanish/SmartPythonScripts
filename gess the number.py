# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:55:59 2019

@author: Rahi
"""

#gess the number 
import random
num= random.choice(range(90))
for chance in range(5,-1,-1):
    z=int(input("gess the number"))
    if z>num:
        print("you gess is too high")
    elif z<num:
        print("your gess is too low")
    else:
        print(f"well done the number is {num}")
        print(f"\nyou complete game in {5-chance} attempt")
        break
    print(f"\nnow you have only {chance} attempt left.")
    if chance==0:
        print ("\n game over!")
        break