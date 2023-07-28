import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 75.2) & (x < 87.58775726407981), np.random.normal(loc=4171534.343603711,scale=0.1, size=x.shape), 0.1*x**5 + 0.2*x**4 + -0.2*x**3 + 2.6*x**2 + 1.2*x**1 + -0.9*x**0)


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


