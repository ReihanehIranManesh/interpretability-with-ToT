import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where(x < -67.3, (-2.1*x**0 + -9.8*x**1 + -2.5*x**2 + 2.7*x**3 + 9.0*x**4) / (8.1*x**0 + 3.1*x**1 + -9.0*x**2 + 5.9*x**3 + -4.6*x**4 + -4.5*x**5), np.random.normal(loc=0.0177036389793448, scale=0.1,size=x.shape))


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


