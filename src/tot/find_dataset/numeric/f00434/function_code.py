import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return (8.4*x**0 + 1.2*x**1) / (-7.3*x**0 + 0.1*x**1 + 2.4*x**2 + -1.0*x**3 + 6.7*x**4)

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


