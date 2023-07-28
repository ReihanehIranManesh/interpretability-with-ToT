import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return (6.4*x**0 + -4.0*x**1 + 2.2*x**2 + 9.7*x**3 + -5.6*x**4) / (3.1*x**0 + -0.4*x**1 + 4.5*x**2 + 8.2*x**3 + -8.2*x**4 + -5.1*x**5)

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


