import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
        return (np.where(abs(x) <= 8.1/2,1,0)) * (-2.6*x**5 + 1.9*x**4 + 1.6*x**3 + -2.1*x**2 + -2.8*x**1 + -1.7*x**0) + np.random.normal(scale=1)

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

