import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return (-2.8*x**0 + 3.2*x**1 + -2.0*x**2) / (-8.4*x**0 + 5.9*x**1 + 6.0*x**2 + -2.0*x**3 + 0.4*x**4)

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


