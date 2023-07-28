import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return (4.5*x**0 + -3.3*x**1 + 9.8*x**2 + -4.2*x**3 + 5.9*x**4) / (-4.3*x**0 + -0.9*x**1 + 1.7*x**2 + -4.1*x**3 + 7.1*x**4 + 3.0*x**5)

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


