from cvxopt.solvers import qp
from cvxopt.base import matrix

import numpy, pylab, random, math


#r = qp(matrix(P), matrix(q), matrix(G), matrix(h))
#alpha = list(r['x'])





#classA = [(random.normalvariate(-1.5,1), random.normalvariate(0.5,1), 1.0)]

def linearKernel(vectorX, vectorY):

    if(len(vectorX)!=len(vectorY)):
        print("Vector length not equal.")
        return 0


    scalar = 0

    for i in range(0,len(vectorX)):
        scalar += vectorX[i]*vectorY[i]

    return (scalar+1)


scalarTest = linearKernel([1,2,3],[1,2,3])
print(scalarTest)
