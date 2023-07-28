import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 26.2) & (x < 36.02294900908707), np.random.normal(loc=64499983.22804444,scale=0.1, size=x.shape), 3.1*x**4 + 4.1*x**3 + -4.1*x**2 + 2.2*x**1 + 0.5*x**0 + -2.3*x**2 + 0.8*x**1 + -2.1*x**0 )


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


