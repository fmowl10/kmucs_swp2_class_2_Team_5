import math
from collections import OrderedDict

import calcFunctions

numPadList = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=',
]

operatorList = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C',
]

CONSTANT_DICT = OrderedDict({
    'pi': math.pi,
    '빛의 이동 속도 (m/s)': 3E+8,
    '소리의 이동 속도 (m/s)': 340,
    '태양과의 평균 거리 (km)': 1.5E+8,
})


FUNCTION_DICT = OrderedDict({
    'factorial (!)': calcFunctions.factorial,
    '-> binary' : calcFunctions.decToBin,
    'binary -> dec': calcFunctions.binToDec,
    '-> roman' : calcFunctions.decToRoman,
    'roman -> binary' : calcFunctions.romanToDec,
})
