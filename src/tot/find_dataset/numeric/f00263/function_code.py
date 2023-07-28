import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > -10.6) & (x < 13.753621124451309), np.random.normal(loc=-1.1997569318530708,scale=0.1, size=x.shape), -2.5 * np.tanh((2 * np.pi / 1.3)*(x-4.5)) + -1.3)


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


