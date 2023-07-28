import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 97.7) & (x < 116.31785748456188), np.random.normal(loc=1.65860878411902,scale=0.1, size=x.shape), -9.4 * np.cos((2 * np.pi / 5.7)*(x-1.8)) + 1.7)


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


