import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 62.8) & (x < 74.22130125753995), np.random.normal(loc=8.200000000000138,scale=0.1, size=x.shape), -8.4 * np.sin((2 * np.pi / 0.5)*(x-2.5)) + 8.2)


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


