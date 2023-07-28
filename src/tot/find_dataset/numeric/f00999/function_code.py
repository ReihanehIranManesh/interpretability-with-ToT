import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return (-4.4*x**0 + 4.6*x**1 + -6.0*x**2 + 8.9*x**3) / (-1.0*x**0 + 9.0*x**1 + -8.3*x**2 + -2.1*x**3 + 7.8*x**4 + -6.4*x**5)

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


