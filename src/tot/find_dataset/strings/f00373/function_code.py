
import numpy as np
import scipy.signal
import sys


def function(string):

    number = 9

    result = ""
    for char in string:
        new_char = chr(ord(char) + number)
        result += new_char
    return result

if __name__ == '__main__':
    outputs = ''
    for arg in sys.argv[1:]:
        string = str(arg)
        outputs += f'({arg}, {str(function(string))}) '

    print(f'Function input - output pairs: {outputs}')
