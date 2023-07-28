import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
        return (-9.3*x**0 + 0.8*x**1) / (6.9*x**0 + -2.5*x**1 + -9.1*x**2 + -4.4*x**3 + -8.0*x**4 + -6.3*x**5) + np.random.normal(scale=1)

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

