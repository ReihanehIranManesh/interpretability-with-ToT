import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > -88.4) & (x < -72.82913432289347), np.random.normal(loc=-3.9959830354594716,scale=0.1, size=x.shape), 6.2 * np.cos((2 * np.pi / 1.8)*(x-1.0)) + -4.1)


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


