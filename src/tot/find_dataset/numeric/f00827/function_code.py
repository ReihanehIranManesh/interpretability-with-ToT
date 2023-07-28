import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
        return (-5.0*x**0 + -1.1*x**1 + 4.2*x**2 + 3.8*x**3) / (8.0*x**0 + 2.1*x**1 + 6.6*x**2 + 6.2*x**3 + 8.7*x**4 + -2.4*x**5) + np.random.normal(scale=1)

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

