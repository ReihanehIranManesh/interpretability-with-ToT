import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):

    return 7.8 * np.cos((2 * np.pi / 2.0)*(x-4.3)) + -3.5

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


