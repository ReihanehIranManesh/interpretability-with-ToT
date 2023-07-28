import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 94.8) & (x < 106.62697914683739), np.random.normal(loc=-8.614839139154618,scale=0.1, size=x.shape), 2.3 * np.sin((2 * np.pi / 2.7)*(x-3.6)) + -8.6)


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


