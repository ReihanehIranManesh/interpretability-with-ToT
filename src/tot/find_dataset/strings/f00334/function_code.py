
import numpy as np
import scipy.signal
import sys


def function(string):

    letter = 'W'

    mid_index = len(string) // 2
    new_string = string[:mid_index] + letter + string[mid_index:]
    return new_string

if __name__ == '__main__':
    outputs = ''
    for arg in sys.argv[1:]:
        string = str(arg)
        outputs += f'({arg}, {str(function(string))}) '

    print(f'Function input - output pairs: {outputs}')
