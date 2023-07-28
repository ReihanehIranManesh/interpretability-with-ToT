import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > -88.6) & (x < -71.05107754040911), np.random.normal(loc=-0.0016295871104439561,scale=0.1, size=x.shape), (4.9*x**0 + -5.0*x**1 + -7.6*x**2 + -9.4*x**3) / (3.8*x**0 + -6.0*x**1 + -9.1*x**2 + -9.6*x**3 + 6.9*x**4))


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


