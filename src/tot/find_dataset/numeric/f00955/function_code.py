import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
        return -9.2 * np.cos((2 * np.pi / 3.2)*(x-4.5)) + -4.3 + np.random.normal(scale=1)

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

