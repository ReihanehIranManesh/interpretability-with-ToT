import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return (-8.8*x**0 + -5.1*x**1 + 8.2*x**2) / (-7.9*x**0 + 8.4*x**1 + 5.4*x**2 + -1.7*x**3)

if __name__ == '__main__':
    outputs = ''
    for arg in sys.argv[1:]:
        x = float(arg)
        try:
            out = function(x)
        except:
            out = 'None'
        outputs += f'({arg}, {out}) '
    print(f'Function input - output pairs: {outputs}')


