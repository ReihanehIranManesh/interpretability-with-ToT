import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > -31.5) & (x < -17.225316330336675), np.random.normal(loc=148.48484848484873,scale=0.1, size=x.shape), 5.1*x + -4.5 + 19.6 * np.where(x > 0, x, x * 0.7) + 4.5 )


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


