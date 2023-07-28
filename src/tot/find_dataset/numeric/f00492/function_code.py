import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 25.7) & (x < 48.49095385511282), np.random.normal(loc=2.7356645765996133,scale=0.1, size=x.shape), 6.8 * np.tanh((2 * np.pi / 4.3)*(x-5.3)) + 3.1)


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


