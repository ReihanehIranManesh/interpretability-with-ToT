import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > -37.8) & (x < -13.034855830090269), np.random.normal(loc=-3.713240221107809,scale=0.1, size=x.shape), -4.7 * np.tanh((2 * np.pi / 4.8)*(x-4.0)) + -3.9)


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


