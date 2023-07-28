import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 12.2) & (x < 33.903636534626166), np.random.normal(loc=-0.024129062841588392,scale=0.1, size=x.shape), (8.5*x**0 + -0.7*x**1) / (-2.6*x**0 + -2.5*x**1 + -4.4*x**2 + -1.9*x**3 + 8.5*x**4 + 8.3*x**5))


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


