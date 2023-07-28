import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > -32.4) & (x < -17.122548533775), np.random.normal(loc=8.301401173038084,scale=0.1, size=x.shape), -7.6 * np.tanh((2 * np.pi / 5.9)*(x-1.3)) + 8.2)


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


