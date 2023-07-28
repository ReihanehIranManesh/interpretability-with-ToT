import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
        return (-10.0*x**0 + 7.7*x**1 + -4.6*x**2) / (7.4*x**0 + 6.8*x**1 + -9.5*x**2 + 9.3*x**3 + -9.7*x**4) + np.random.poisson(lam=1)

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

