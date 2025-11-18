import math

def add(a,b): return a+b
def subtract(a,b): return a-b
def multiply(a, b): return a * b
def divide(a, b): 
    if b == 0: 
        raise ZeroDivisionError 
    else: return a / b  # raise ZeroDivisionError if a == 0 
def logarithm(a, b): 
    if b == 0:
         raise ValueError 
    else: return math.log(b,a)# use math library/raise ValueError
def exponent(a, b): return a**b
