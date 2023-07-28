import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where(x < 25.1, (5.6*x**0 + 4.9*x**1 + -9.8*x**2 + 4.3*x**3) / (0.2*x**0 + 3.6*x**1 + 1.5*x**2 + -0.1*x**3 + 9.7*x**4), np.random.normal(loc=-0.01772272727662034, scale=0.1,size=x.shape))


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


