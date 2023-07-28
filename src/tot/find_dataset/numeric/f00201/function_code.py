import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
        return 13.3 * np.where(x > 0, x, x * 0.6) + 1.3 + -0.2*x**2 + -1.1*x**1 + 3.7*x**0  + np.random.poisson(lam=1)

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

