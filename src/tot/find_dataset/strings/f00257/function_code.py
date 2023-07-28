
import numpy as np
import scipy.signal
import sys


def function1(string):

    if string == "" or not string[-1].isalpha():
        return string
    elif string[-1] == 'a':  # wrap around from 'a' to 'y'
        return string[:-1] + 'y'
    elif string[-1] == 'b':  # wrap around from 'b' to 'z'
        return string[:-1] + 'z'
    elif string[-1] == 'A':  # wrap around from 'A' to 'Y'
        return string[:-1] + 'Y'
    elif string[-1] == 'B':  # wrap around from 'B' to 'Z'
        return string[:-1] + 'Z'
    else:
        return string[:-1] + chr(ord(string[-1]) - 2)


def function2(string):

    old = 'p'
    new = 'F'

    return string.replace(old, new)

def function(string):
    return function1(function2(string))

if __name__ == '__main__':
    outputs = ''
    for arg in sys.argv[1:]:
        string = str(arg)
        outputs += f'({arg}, {str(function(string))}) '

    print(f'Function input - output pairs: {outputs}')
