from math import factorial as fact
from keypad import numPadList, operatorList


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

romansThings = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

def decToRoman(numStr):
    try:
        n = int(numStr)
        r = ''
        if n <= 10000:
            for value, letters in romansThings:
                while n >= value:
                    r += letters
                    n -= value
        else:
            r = 'Error!'
    except ValueError:
        r = 'Error!'
    return r

def romanToDec(numStr):
    s = str(numStr)
    n = 0
    for value, letters in romansThings:
        while s.find(letters) == 0:
            n += value
            s = s[len(letters):]

    # other solution
    #    while s[:len(letters)] == letters:
    #         n += value
    #         s = s[len(letters):]

    for i in range(len(s)):
        if s[i] in numPadList or s[i] in operatorList:
            n = str('Error!')
            break
    return n
