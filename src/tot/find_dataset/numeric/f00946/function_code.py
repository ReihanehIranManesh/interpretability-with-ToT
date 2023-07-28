import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return (-0.9*x**0 + -8.9*x**1 + -3.1*x**2 + 5.3*x**3 + -2.5*x**4) / (-0.1*x**0 + 9.9*x**1 + 5.5*x**2 + 6.8*x**3 + -6.5*x**4 + 4.7*x**5)

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


