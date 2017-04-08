# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math

def sum(first, second):
    return first + second

def subtract(first, second):
    return first - second
    
def multiply(first, second):
    return first * second
    
def divide(first, second):
    try:
        return round((first * 1.0) / (second * 1.0),2)
    except:
        return 'undefined'
    
def exponent(first, second):
    return first ** second

def square_root(number):
    return round(math.sqrt(number),2)

def cube(number):
    return round(number * number * number,2)

def sine(number):
    return round(math.sin(number),2)

def factoryal(number):
    try:
        return math.factorial(number)
    except:
        return 'not allowed'
        
    
