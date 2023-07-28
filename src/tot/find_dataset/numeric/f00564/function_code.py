import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 21.8) & (x < 26.833665717536164), np.random.normal(loc=-6.299999999999999,scale=0.1, size=x.shape), -11.2*np.heaviside(x, 45.5)+ -0.7 + np.where(x > 0, 1, -1) )


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


