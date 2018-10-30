from math import factorial as fact

def factorial(numStr):
    try:
        if int(numStr) <= 17:   # 17!까지 15자리 수이므로
            r = str(fact(int(numStr)))
        elif int(numStr) > 17:
            r = 'Error!'
    except ValueError:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        if int(numStr) < 32768: # 32767을 이진수로 변환하면 111111111111111 이므로
            r = bin(int(numStr))[2:]
        elif int(numStr) >= 32768:
            r = 'Error!'
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

# decToRoman, romanToDec 함수에서 모두 사용하므로 바깥에 배치한다.
romans = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]

def decToRoman(numStr):
    try:
        n = int(numStr)

        if n >= 4000:
            return 'Error!'
        elif n == 0:
            return 'Error!'

        result = ''
        for value, letters in romans:
            while n >= value:
                result += letters
                n -= value
    except:
        return 'Error!'
    return result

def romanToDec(numStr):
    try:
        n = str(numStr)
        result = 0

        for value, letters in romans:
            while n != '':
                if n[:2] == letters:
                    result += value
                    n = n[2:]
                elif n[0] == letters:
                    result += value
                    n = n[1:]
                else:
                    break
    except:
        result = "Error!"
    return result
