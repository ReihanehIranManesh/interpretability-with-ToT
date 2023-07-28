import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 98.0) & (x < 105.57668523169013), np.random.normal(loc=39539804.63645647,scale=0.1, size=x.shape), 1.9*x**4 + 0.6*x**3 + -1.7*x**2 + 1.6*x**1 + -2.4*x**0)


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


