import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return (1.0*x**0 + 2.2*x**1 + -9.3*x**2 + -7.8*x**3 + -1.9*x**4) / (-1.7*x**0 + 5.1*x**1 + 0.6*x**2 + 6.0*x**3 + -5.7*x**4 + 6.7*x**5)

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


