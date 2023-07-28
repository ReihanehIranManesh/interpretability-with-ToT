import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > -85.9) & (x < -75.38494633476209), np.random.normal(loc=6357.671515151517,scale=0.1, size=x.shape), (-0.2 * np.where(x > 0, x, x * 0.5) + 6.4) * (-16.8 * np.where(x > 0, x, x * 0.6) + 4.3))


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


