import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return (5.5*x**0 + -0.4*x**1) / (-8.2*x**0 + -9.2*x**1 + -3.7*x**2 + -7.6*x**3 + 5.6*x**4 + 9.6*x**5)

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


