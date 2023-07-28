import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 24.8) & (x < 32.56724885822773), np.random.normal(loc=0.02,scale=0.1, size=x.shape), np.where(abs(x) <= 1.5/2,1,0) + np.where(x > 0, 1, -1) )


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


