import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where(x < -7.9, (-4.7*x**0 + -7.0*x**1 + 9.6*x**2 + 1.0*x**3 + 8.7*x**4) / (9.8*x**0 + 8.9*x**1 + 8.7*x**2 + -4.1*x**3 + 0.1*x**4 + 5.3*x**5), np.random.normal(loc=0.02597119489073946, scale=0.1,size=x.shape))


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


