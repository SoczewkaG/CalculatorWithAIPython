'''
TODO
sqrt

absolute
negate

modulo

percentage

factorial

reciprocal
square
cube
'''

def add(a: float, b: float) -> float:
    """
    Adding a to b
    """
    return a+b



def substract(a: float, b: float) -> float:
    """
    Substract a from b
    """
    return a-b



def multiply(a: float, b: float) -> float:
    """
    Multiplies a times b
    """
    return a*b



def divide(a: float, b: float) -> float:
    """
    Divides a by b
    """
    return a/b



def power(a: float, b: float) -> float:
    """
    Raises a to the power of B
    """
    return pow(a,b)



def sqrt(a: float) -> float:
    """
    returns the square root of a
    """
    if a < 0:
        return "Invalid input"
    return sqrt(a)

#print("Dodawanie 2+2=", add(2, 2))
#print("Odejmowanie 2-2=", substract(2, 2))
#print("Mnozenie 2*2=", multiply(2, 2))
#print("Dzielenie 2/2=", divide(2, 2))