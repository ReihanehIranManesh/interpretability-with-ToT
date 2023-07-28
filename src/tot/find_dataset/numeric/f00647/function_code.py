import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return (-7.9*x**0 + 8.1*x**1 + -9.8*x**2) / (2.0*x**0 + -3.9*x**1 + -4.0*x**2 + -5.1*x**3)

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


