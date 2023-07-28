import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where(x > 20.3, (-8.0*x**0 + -7.7*x**1) / (8.6*x**0 + 8.5*x**1 + 1.0*x**2 + -1.8*x**3), np.random.normal(loc=0.052380931320388936,scale=0.1, size=x.shape))


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


