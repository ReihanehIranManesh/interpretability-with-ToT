import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
        return (1.9*x**0 + -9.8*x**1) / (-4.9*x**0 + -8.6*x**1 + -5.9*x**2 + -6.5*x**3 + 3.4*x**4 + 6.9*x**5) + np.random.normal(scale=1)

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

