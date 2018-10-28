from collections import OrderedDict
from math import factorial as fact

ROMAN_NUMBER = OrderedDict({
    1000:'M', 500:'D',
    100:'C', 50:'L',
    10:'X', 5:'V',
    1:'I',
})

REVERSED_ROMAN_NUMBER = OrderedDict({v:k for k, v in ROMAN_NUMBER.items()})

# if method get bigger than 99999 raise Exception
def factorial(numStr):
    try:
        n = int(numStr)
        if n >= 1000000:
            raise Exception
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    '''
        This method convert given Arabic numeral to roman numeral.
        When the method returns error message
            got Roman number
            got number that over 4000
    '''
    result_roman = ''
    try:
        if isRoman(numStr):
            raise Exception
        n = int(numStr)
        if n >= 4000:
            raise Exception
        for unit in ROMAN_NUMBER.keys():
            div, n = divmod(n, unit)
            if div == 4:
                if result_roman and result_roman[-1] == ROMAN_NUMBER[unit * 5]:
                    result_roman = result_roman[:-1]
                    result_roman += ROMAN_NUMBER[unit] + ROMAN_NUMBER[unit * 10]
                else:
                    result_roman += ROMAN_NUMBER[unit] + ROMAN_NUMBER[unit * 5]
                continue
            result_roman += ROMAN_NUMBER[unit] * div
    except:
        result_roman = 'Error!'
    return result_roman

def romanToDec(numStr):
    '''
        This method convert given romman numeral to Arabic numeral.
        When the method returns error message
            got non-roman number
            got empty string then retuns error message.
            got wrong form
    '''
    result_dec = 0
    result_arr = []
    try:
        if not isRoman(numStr):
            raise Exception
        if not numStr:
            raise Exception
        stack = []
        for idx in range(len(numStr)):
            if not stack:
                stack.insert(0, numStr[idx])
                continue
            if len(stack) > 1:
                stack_last = REVERSED_ROMAN_NUMBER[stack[-1]]
                current_idx = REVERSED_ROMAN_NUMBER[numStr[idx]]
                if stack_last < current_idx:
                    raise Exception
            if REVERSED_ROMAN_NUMBER[stack[-1]] == REVERSED_ROMAN_NUMBER[numStr[idx]]:
                roman_duplicatable = [k for k in ROMAN_NUMBER.keys() if str(k // 5)[0] != '1']
                if REVERSED_ROMAN_NUMBER[numStr[idx]] not in roman_duplicatable:
                    raise Exception

            if REVERSED_ROMAN_NUMBER[stack[-1]] > REVERSED_ROMAN_NUMBER[numStr[idx]]:
                temp = romanStack(stack)
                result_arr.append(str(temp))
                result_dec += temp
            stack.insert(0, numStr[idx])
        else:
            result_dec += romanStack(stack)
        
        for x in result_arr:
            if len(x) > 1:
                raise Exception
    except:
        result_dec = 'Error!'
    return result_dec

def romanStack(stack):
    '''
        This method reduces stack
        When the method returns -1
            exception KeyError
    '''
    result_stack = 0
    while len(stack) > 1:
        try:
            num_i = REVERSED_ROMAN_NUMBER[stack.pop()]
            num_j = REVERSED_ROMAN_NUMBER[stack.pop()]
        except KeyError:
            return -1
        if num_i != num_j:
            # if num_i is smaller than num_j
            result_stack += num_j - num_i
        else:
            # if num_i and num_j are same
            result_stack += num_i + num_j
    if stack:
        # add last number
        result_stack += REVERSED_ROMAN_NUMBER[stack.pop()]
    return result_stack

def isRoman(numStr):
    '''
        This method returns "True" if given number is the Roman numeral.
        Otherwise returns "False"
    '''
    for s in numStr:
        if s not in ROMAN_NUMBER.values():
            return False
    return True
