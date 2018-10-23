from math import factorial as fact

# all function get float raise exception

def factorial(numStr):
    try:
        if not isinstance(numStr, int):
            raise Exception
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        if not isinstance(numStr, int):
            raise Exception
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        if not isinstance(numStr, int):
            raise Exception
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    return 'Error!'
