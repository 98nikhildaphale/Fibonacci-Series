# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 21:13:28 2021


"""


x=int(input("Enter the no of Terms: "))

a=0
b=1



for i in range(x):
    print(a)
    c=a
    a=b
    b=c+b
    
