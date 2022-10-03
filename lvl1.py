# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 13:08:08 2022

@author: dimit
"""
import math
def primetest(n):
     for i in range(2, int(math.sqrt(n))+1):
        if (n%i== 0):
            return False
 
     return True
def solution(i):
    stringy=''
    k=1
    while len(stringy)<10000:
        k+=1
        if primetest(k):
            stringy+=str(k)
    return stringy[i:i+5]
        
    