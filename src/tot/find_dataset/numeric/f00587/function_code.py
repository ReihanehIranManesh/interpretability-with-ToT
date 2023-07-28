import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 35.2) & (x < 41.762822585761555), np.random.normal(loc=1.3614400181856232,scale=0.1, size=x.shape), (8.5*x**0 + -0.0*x**1 + -4.9*x**2 + 7.6*x**3 + 8.1*x**4) / (4.8*x**0 + 1.0*x**1 + -7.8*x**2 + -9.7*x**3 + -5.1*x**4 + -0.7*x**5))


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


