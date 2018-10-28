from collections import OrderedDict
from math import factorial as fact

class RomanError(Exception):
    '''
        special exception for roman converter
    '''
    def __init__(self, error_message):
        super(RomanError, self).__init__(error_message)

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

def decToRoman(numStr: str) -> str:
    '''
        This method convert given Arabic numeral to roman numeral.
        When the method returns error message
            got Roman number
            got number that over 4000
    '''
    result_roman = ''
    try:
        if isRoman(numStr):
            raise RomanError('not an Arabic numeral')
        n = int(numStr)
        if n >= 4000:
            raise RomanError('too big Arabic numeral')
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
    except RomanError:
        return 'Error!'
    return result_roman

def romanToDec(numStr: str) -> str:
    '''
        This method convert given romman numeral to Arabic numeral.
        When the method returns error message
            got non-roman number
            got empty string then retuns error message.
            got wrong form
    '''
    result_dec = 0
    try:
        if not isRoman(numStr):
            raise RomanError('Not an Roman numeral')
        if not numStr:
            raise TypeError
        stack = []
        for _, current_idx in enumerate(numStr):
            current_idx = REVERSED_ROMAN_NUMBER[current_idx]
            try:
                stack_last = stack[-1]
            except IndexError:
                stack.insert(0, current_idx)
                continue

            if len(stack) > 1:
                if stack_last < current_idx:
                    raise RomanError('Wrong form')
            if stack_last == current_idx:
            # the same letter can't be 4 letters
                if stack.count(stack_last) > 3:
                    raise RomanError('Wrong form')
                roman_duplicatable = [k for k in ROMAN_NUMBER.keys() if str(k // 5)[0] != '1']
                if current_idx not in roman_duplicatable:
                    raise RomanError('Wrong form')

            if stack_last > current_idx:
                temp = romanStack(stack)
                result_dec += temp
            stack.insert(0, current_idx)

        if stack:
            result_dec += romanStack(stack)
    except RomanError:
        return 'Error!'
    except TypeError:
        return 'Error!'
    return str(result_dec)

def romanStack(stack: list):
    '''
        This method reduces stack
        When the method returns -1
            exception KeyError
    '''
    result_stack = 0
    while len(stack) > 1:
        num_i = stack.pop()
        num_j = stack.pop()
        if num_i != num_j:
            # if num_i is smaller than num_j
            result_stack += num_j - num_i
        else:
            # if num_i and num_j are same
            result_stack += num_i + num_j
    if stack:
        # add last number
        result_stack += stack.pop()
    return result_stack

def isRoman(numStr: str) -> bool:
    '''
        This method returns "True" if given number is the Roman numeral.
        Otherwise returns "False"
    '''
    for s in numStr:
        if s not in ROMAN_NUMBER.values():
            return False
    return True
