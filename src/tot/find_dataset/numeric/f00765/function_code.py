import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):


    return (1 / (2.1 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - -27.7) / 2.1) ** 2)

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


