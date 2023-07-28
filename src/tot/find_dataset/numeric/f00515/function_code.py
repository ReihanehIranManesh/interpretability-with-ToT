import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return (-1.8*x**0 + -3.5*x**1 + -2.8*x**2 + 2.8*x**3) / (-9.3*x**0 + 6.9*x**1 + 7.4*x**2 + -9.3*x**3 + -5.4*x**4)

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


