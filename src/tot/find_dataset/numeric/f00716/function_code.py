import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 79.9) & (x < 86.00124117365105), np.random.normal(loc=0.04581914382864254,scale=0.1, size=x.shape), (-3.8*x**0 + 0.2*x**1 + 2.9*x**2 + -7.8*x**3) / (2.7*x**0 + -2.3*x**1 + 7.7*x**2 + -8.6*x**3 + -3.1*x**4))


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


