
import numpy as np
import scipy.signal
import sys


def function1(string):

    letter = 'K'

    if not string.endswith(letter):
        string += letter
    return string


def function2(string):

    new_string = 'INShH'

    return string + new_string

def function(string):
    return function1(function2(string))

if __name__ == '__main__':
    outputs = ''
    for arg in sys.argv[1:]:
        string = str(arg)
        outputs += f'({arg}, {str(function(string))}) '

    print(f'Function input - output pairs: {outputs}')