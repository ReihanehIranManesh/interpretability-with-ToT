import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return (6.4*x**0 + 4.2*x**1 + -9.1*x**2 + 4.9*x**3 + 4.9*x**4) / (-2.8*x**0 + -0.6*x**1 + -8.3*x**2 + 2.9*x**3 + 5.9*x**4 + -8.9*x**5)

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


