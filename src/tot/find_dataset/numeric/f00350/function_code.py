import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > -29.7) & (x < -21.560328660481893), np.random.normal(loc=5.820364717553327,scale=0.1, size=x.shape), -0.5 * np.tanh((2 * np.pi / 3.0)*(x-4.3)) + 5.8)


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


