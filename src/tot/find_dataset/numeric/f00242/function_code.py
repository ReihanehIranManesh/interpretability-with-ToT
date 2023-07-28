import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 73.1) & (x < 95.52224343506658), np.random.normal(loc=0.05233200556468669,scale=0.1, size=x.shape), 7.6 * np.tanh((2 * np.pi / 4.1)*(x-3.2)) + 0.3)


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


