from cvxopt.solvers import qp
from cvxopt.base import matrix

import numpy, pylab, random, math


def main():
    data = generateData()
    pMatrix = pMatrixCreator(data)
    q,h = qhVectorCreator(len(data))
    gMatrix = gMatrixCreator(len(data))
    #print(pMatrix[0][0])
    r = qp(matrix(pMatrix), matrix(q), matrix(gMatrix), matrix(h))
    alpha = list(r['x'])
    svm = nonZeroAlphas(data, alpha)
    res = indicator((1.25,1),svm)
    #print(res)

    plotDB(svm,data)

def plotDB(svm,data):


    xrange=numpy.arange(-4,4,0.05)
    yrange =numpy.arange(-4,4,0.05)

    grid=matrix([[indicator((x,y),svm)
                for y in yrange]
                for x in xrange])

    pylab.contour(xrange,yrange,grid,(-1.0,0.0,1.0),colors=('red','black','blue'),linewidths=(1,3,1))
    pylab.show()


def nonZeroAlphas(data, alpha):
    values = []
    for i in range(len(alpha)):
        if alpha[i] > 10**-5:
            values.append((data[i][0] ,data[i][1], data[i][2], alpha[i]))

    return values

def indicator(dataPoint, svm):
    res = 0.0
    for tup in svm:
        res += tup[3]*tup[2]*polynomialKernel(dataPoint, tup[0:2])
    return res



def linearKernel(vectorX, vectorY):
    if(len(vectorX)!=len(vectorY)):
        print("Vector length not equal.")
        return 0.0
    scalar = 0.0
    for i in range(0,len(vectorX)):
        scalar += vectorX[i]*vectorY[i]
    return scalar+1.0

def polynomialKernel(vectorX, vectorY):
    if(len(vectorX)!=len(vectorY)):
        print("Vector length not equal.")
        return 0
    scalar = 0.0
    for i in range(0,len(vectorX)):
        scalar += vectorX[i]*vectorY[i]
    return (scalar+1.0)**2


def pMatrixCreator(dataSet):
    n = len(dataSet)
    pMatrix = [[0.0 for x in range(n)] for y in range(n)]
    for i in range(n):
        x = dataSet[i]
        for j in range(n):
            y = dataSet[j]
            pMatrix[i][j] = x[2]*y[2]*polynomialKernel(x[:2] ,y[:2])
    return pMatrix

def qhVectorCreator(n):
    q = [-1.0]*n
    h = [0.0]*n
    return [q],[h]

def gMatrixCreator(n):
    gMatrix = [[0.0 for x in range(n)] for y in range(n)]
    for i in range(n):
        gMatrix[i][i] = -1.0
    return gMatrix

def generateData():
    random.seed(100)
    classA = [(random.normalvariate(-1.5 ,1),
        random.normalvariate(0.5 ,1),
        1.0)
        for i in range(5)] + \
        [(random.normalvariate(1.5 ,1),
        random.normalvariate(0.5 ,1),
        1.0)
        for i in range(5)]
    classB = [(random.normalvariate(0.0 ,0.5),
        random.normalvariate(-0.5 ,0.5),
        -1.0) for i in range(10)]
    data = classA + classB
    random.shuffle(data)

    pylab.hold(True)
    pylab.plot( [p[0] for p in classA],
                [p[1] for p in classA],'bo')
    pylab.plot( [p[0] for p in classB],
                [p[1] for p in classB], 'ro')
    #pylab.show()


    return data




if __name__ == '__main__':
    main()
