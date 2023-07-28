import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where(x > -24.0, (-6.9*x**0 + -1.7*x**1 + 6.5*x**2 + -2.6*x**3 + 1.2*x**4) / (-6.3*x**0 + -2.5*x**1 + 4.4*x**2 + 5.5*x**3 + 6.0*x**4 + -0.9*x**5), np.random.normal(loc=0.03796300990202786,scale=0.1, size=x.shape))


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


