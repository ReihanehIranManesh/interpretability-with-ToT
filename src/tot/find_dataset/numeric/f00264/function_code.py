import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
        return (2.2*x**0 + -9.5*x**1) / (-2.6*x**0 + -0.2*x**1 + 5.5*x**2 + 3.4*x**3 + -2.3*x**4 + -3.4*x**5) + np.random.poisson(lam=1)

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

