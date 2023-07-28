import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    return (4.5*x**5 + 2.8*x**4 + -1.5*x**3 + 1.6*x**2 + -3.4*x**1 + -2.1*x**0) * (np.floor(x))

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


