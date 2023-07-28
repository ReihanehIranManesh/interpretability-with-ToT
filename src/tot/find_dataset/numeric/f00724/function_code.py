import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
        return (-9.9*x**0 + 7.7*x**1 + -9.7*x**2 + 6.6*x**3) / (-8.7*x**0 + 9.7*x**1 + 3.1*x**2 + 3.1*x**3 + 6.9*x**4) + np.random.normal(scale=1)

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

