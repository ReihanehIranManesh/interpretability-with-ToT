import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return (-9.2*x**0 + 9.0*x**1 + -5.5*x**2 + 9.7*x**3 + 5.8*x**4) / (1.3*x**0 + -0.8*x**1 + -9.3*x**2 + 0.4*x**3 + -6.0*x**4 + -6.4*x**5)

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


