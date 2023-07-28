import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return (6.9*x**0 + 2.7*x**1 + -1.0*x**2 + -0.7*x**3) / (6.7*x**0 + 3.6*x**1 + -7.4*x**2 + 9.8*x**3 + -8.8*x**4 + -0.3*x**5)

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


