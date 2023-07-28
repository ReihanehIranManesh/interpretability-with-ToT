import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    return -2.9*x**4 + 1.5*x**3 + -0.4*x**2 + 4.2*x**1 + 0.2*x**0 + 11.0 * np.where(x > 0, x, x * 0.9) + -0.9 

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


