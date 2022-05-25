import numpy as np  
import numpy.matlib  
import math

def run(x, y):
    xt = np.matrix.getT((np.matrix(x)))
    n = np.matrix.getI((xt*np.matrix(x)))
    return n*(xt*np.matrix(y))

x = [[1, 1], [2, 1], [3, 1]]
y = [[math.log(2)], [math.log(5)], [math.log(10)]]

print(run(x, y))