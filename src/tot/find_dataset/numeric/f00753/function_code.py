import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where(x < -81.4, (1 / (2.5 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - -5.0) / 2.5) ** 2), np.random.normal(loc=0.0049500000000007385, scale=0.1,size=x.shape))


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


