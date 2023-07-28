import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return (-2.8*x**0 + -5.7*x**1 + 2.5*x**2 + 8.2*x**3 + -0.8*x**4) / (4.5*x**0 + -7.6*x**1 + -9.4*x**2 + 0.3*x**3 + 4.2*x**4 + -5.3*x**5)

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


