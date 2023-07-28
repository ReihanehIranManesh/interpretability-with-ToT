import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 2.5) & (x < 13.931806578487183), np.random.normal(loc=-1.5500407667502998,scale=0.1, size=x.shape), -7.8 * np.cos((2 * np.pi / 0.3)*(x-3.7)) + -1.5)


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


