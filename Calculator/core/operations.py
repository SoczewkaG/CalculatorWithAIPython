def add(a: float, b: float) -> float:
    """
    Adding A to B
    """
    return a+b



def substract(a: float, b: float) -> float:
    """
    Substract A from B
    """
    return a-b



def multiply(a: float, b: float) -> float:
    """
    Multiplies A times B
    """
    return a*b



def divide(a: float, b: float) -> float:
    """
    Divides A by B
    """
    return a/b



def power(a: float, b: float) -> float:
    """
    Raises A to the power of B
    """
    return pow(a,b)



def sqrt(a: float) -> float:
    """
    returns the square root of A,
    value need to be higher than 0
    """
    if a < 0:
        return "Invalid input"
    return sqrt(a)



def absolute(a: float) ->  float:
    """
    returns absoulute value of A
    """
    return abs(a)



def negate(a: float) -> float:
    """
    changes a sign of a number to the opposite
    """
    return -a



def modulo(a: float, b: float) -> float:
    """
    returns the last of the division A/B
    """
    return a % b



def percentage(a: float, b: float) -> float:
    """
    returns what % of number B is number A
    """
    return (a/b) * 100



def factorial(a: float) -> float:
    """
    returns a factorial of number A
    """
    if a == 0: 
        return 1
    else:
        return a * factorial(a - 1)



def reciprocal(a: float) -> float:
    """
    returns a reciprocal value of number A
    """
    return 1/a



def square(a: float) -> float:
    """
    returns a square value of number A
    """
    return a*a



def cube(a: float) -> float:
    """
    returns a cube of value A
    """
    return a*a*a