import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > -35.3) & (x < -14.15959697674252), np.random.normal(loc=49.3290101010101,scale=0.1, size=x.shape), (np.where(x > 0, 1, -1)) * (-22.9 * np.where(x > 0, x, x * 1.0) + 8.6))


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


