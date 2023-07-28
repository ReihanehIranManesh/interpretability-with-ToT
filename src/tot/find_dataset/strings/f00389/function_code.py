
import numpy as np
import scipy.signal
import sys


def function1(string):

    return string.upper()


def function2(string):

    substring = 'C'

    return string.replace(substring, '')

def function(string):
    return function1(function2(string))

if __name__ == '__main__':
    outputs = ''
    for arg in sys.argv[1:]:
        string = str(arg)
        outputs += f'({arg}, {str(function(string))}) '

    print(f'Function input - output pairs: {outputs}')
