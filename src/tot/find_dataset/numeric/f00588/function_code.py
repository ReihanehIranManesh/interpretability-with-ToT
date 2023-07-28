import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where(x > 34.7, (8.6*x**0 + -3.7*x**1 + 1.5*x**2 + -8.8*x**3 + 4.8*x**4) / (7.0*x**0 + -1.9*x**1 + 9.6*x**2 + 7.2*x**3 + 3.9*x**4 + 9.8*x**5), np.random.normal(loc=0.05097938281452244,scale=0.1, size=x.shape))


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


