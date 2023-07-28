import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 45.9) & (x < 55.12058099073596), np.random.normal(loc=0.02574617047462438,scale=0.1, size=x.shape), (-5.8*x**0 + -9.7*x**1) / (7.5*x**0 + -6.6*x**1 + -9.0*x**2))


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


