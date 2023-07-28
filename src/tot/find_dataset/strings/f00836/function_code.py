
import numpy as np
import scipy.signal
import sys


def function1(string):

    if string == "" or not string[-1].isalpha():
        return string
    elif string[-1] == 'y':  # wrap around from 'y' to 'a'
        return string[:-1] + 'a'
    elif string[-1] == 'z':  # wrap around from 'z' to 'b'
        return string[:-1] + 'b'
    elif string[-1] == 'Y':  # wrap around from 'Y' to 'A'
        return string[:-1] + 'A'
    elif string[-1] == 'Z':  # wrap around from 'Z' to 'B'
        return string[:-1] + 'B'
    else:
        return string[:-1] + chr(ord(string[-1]) + 2)


def function2(string):

    number = 1

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
