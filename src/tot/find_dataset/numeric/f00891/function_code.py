import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 9.5) & (x < 16.188659395470506), np.random.normal(loc=-0.003169392639972476,scale=0.1, size=x.shape), (2.4*x**0 + 1.6*x**1 + 4.9*x**2) / (5.5*x**0 + 5.6*x**1 + -8.4*x**2 + 5.6*x**3 + 8.9*x**4))


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


