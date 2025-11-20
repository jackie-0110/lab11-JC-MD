#https://github.com/jackie-0110/lab11-JC-MD
import math

def square_root(a): 
    if a < 0: 
        raise ValueError
    else:
        math.sqrt(a)
def hypotenuse(a, b): math.hypot(a, b) # can have negative nums
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
def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(a)
    except ValueError:
        raise   

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)  
    except ValueError:
        raise