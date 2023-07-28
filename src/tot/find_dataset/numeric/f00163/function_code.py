import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf


def function(x):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where(x < 93.2, (-17.1 * np.where(x > 0, x, x * 0.8) + -0.7) * (23.7 * np.where(x > 0, x, x * 0.5) + -2.1), np.random.normal(loc=-964760.2724242427, scale=0.1,size=x.shape))


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


