import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 32.1) & (x < 49.27805570293987), np.random.normal(loc=-1.8999999999999926,scale=0.1, size=x.shape), 7.6 * np.sin((2 * np.pi / 0.8)*(x-4.0)) + -1.9)


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


