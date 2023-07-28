import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return (0.5*x**0 + -7.1*x**1 + 5.1*x**2 + 6.4*x**3) / (4.8*x**0 + 7.4*x**1 + -6.0*x**2 + 3.6*x**3 + 0.0*x**4 + 7.7*x**5)

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


