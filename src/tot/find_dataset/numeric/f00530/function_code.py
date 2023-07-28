import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 9.4) & (x < 29.267300392907416), np.random.normal(loc=8.00000000000004,scale=0.1, size=x.shape), 3* np.ones_like(x) + 6.3*x + 5.0 )


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


