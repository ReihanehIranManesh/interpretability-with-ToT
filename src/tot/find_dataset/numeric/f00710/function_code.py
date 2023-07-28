import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > -75.2) & (x < -53.338604509355875), np.random.normal(loc=4.095637028825665,scale=0.1, size=x.shape), 3.9 * np.sin((2 * np.pi / 5.6)*(x-6.0)) + 4.1)


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


