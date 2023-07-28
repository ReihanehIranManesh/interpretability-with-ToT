import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > -11.8) & (x < 6.610602814159815), np.random.normal(loc=0.004949999999999999,scale=0.1, size=x.shape), (1 / (7.4 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - 15.1) / 7.4) ** 2))


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


