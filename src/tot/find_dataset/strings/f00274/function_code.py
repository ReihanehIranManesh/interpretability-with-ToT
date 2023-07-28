
import numpy as np
import scipy.signal
import sys


def function1(string):

    return ''.join(sorted(set(string), key=string.index))


def function2(string):

    number = 2

    result = ""
    for char in string:
        new_char = chr(ord(char) + number)
        result += new_char
    return result

def function(string):
    return function1(function2(string))

if __name__ == '__main__':
    outputs = ''
    for arg in sys.argv[1:]:
        string = str(arg)
        outputs += f'({arg}, {str(function(string))}) '

    print(f'Function input - output pairs: {outputs}')
