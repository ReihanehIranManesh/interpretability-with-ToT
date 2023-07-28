import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > 96.1) & (x < 114.69920496127885), np.random.normal(loc=0.9022430662599641,scale=0.1, size=x.shape), -0.7 * np.sin((2 * np.pi / 5.2)*(x-5.8)) + 0.9)


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


