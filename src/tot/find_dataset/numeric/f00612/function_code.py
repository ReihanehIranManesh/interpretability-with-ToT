import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
        return (-3.0*x**0 + -0.1*x**1 + 1.9*x**2 + 9.4*x**3 + -4.2*x**4) / (7.7*x**0 + 6.8*x**1 + -0.1*x**2 + -8.5*x**3 + 7.2*x**4 + 2.8*x**5) + np.random.normal(scale=1)

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

