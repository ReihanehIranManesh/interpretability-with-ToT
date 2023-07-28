import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > -31.3) & (x < -23.267969325809776), np.random.normal(loc=-0.3681956876127039,scale=0.1, size=x.shape), (9.2*x**0) / (-5.3*x**0 + -5.0*x**1))


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


