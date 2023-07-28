import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > -49.8) & (x < -29.05164869924057), np.random.normal(loc=-3397.93340067346,scale=0.1, size=x.shape), -0.7*x**3 + -1.0*x**2 + 1.3*x**1 + 2.7*x**0 + np.where(abs(x) <= 8.5/2,1,0) )


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


