from math import factorial as fact


def factorial(numStr):
    try:
        if int(numStr) <= 10000:
            r = str(fact(int(numStr)))
        elif int(numStr) > 10000:
            r = 'Error!'
    except ValueError:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except ValueError:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except ValueError:
        r = 'Error!'
    return r

def decToRoman(numStr):
    return 'dec -> Roman'
