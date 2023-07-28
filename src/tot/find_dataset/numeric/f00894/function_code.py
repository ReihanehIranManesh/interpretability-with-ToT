import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    return (19.4 * np.where(x > 0, x, x * 1.0) + 7.6) * (4.0*x**5 + -0.8*x**4 + -0.9*x**3 + -0.9*x**2 + 4.1*x**1 + -1.7*x**0)

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


