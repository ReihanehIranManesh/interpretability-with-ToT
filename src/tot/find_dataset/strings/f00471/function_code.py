
import numpy as np
import scipy.signal
import sys


def function1(string):

    old = 'S'
    new = 'U'

    return string.replace(old, new)


def function2(string):

    return ''.join(string.split())

def function(string):
    return function1(function2(string))

if __name__ == '__main__':
    outputs = ''
    for arg in sys.argv[1:]:
        string = str(arg)
        outputs += f'({arg}, {str(function(string))}) '

    print(f'Function input - output pairs: {outputs}')