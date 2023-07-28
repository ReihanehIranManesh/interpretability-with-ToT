import numpy as np
import scipy.signal
import sys
from scipy.special import gamma, factorial, erf




def function(x):


    return (1 / (4.2 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - -20.1) / 4.2) ** 2)

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


