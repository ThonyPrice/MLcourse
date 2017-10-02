from cvxopt.solvers import qp
from cvxopt.base import matrix

import numpy, pylab, random, math


#r = qp(matrix(P), matrix(q), matrix(G), matrix(h))
#alpha = list(r['x'])

def main():
    data = generateData()
    #print(data)
    pMatrix = pMatrixCreator(data)
    q,h = qhVectorCreator(len(data))
    #print(len(q))
    #print(len(pMatrix))
    gMatrix = gMatrixCreator(len(data))

    r = qp(matrix(pMatrix), matrix(q), matrix(gMatrix), matrix(h))
    alpha = list(r['x'])
    #print('\n' + str(alpha))



#classA = [(random.normalvariate(-1.5,1), random.normalvariate(0.5,1), 1.0)]

def linearKernel(vectorX, vectorY):

    if(len(vectorX)!=len(vectorY)):
        print("Vector length not equal.")
        return 0


    scalar = 0

    for i in range(0,len(vectorX)):
        scalar += vectorX[i]*vectorY[i]

    return (scalar+1.0)


def pMatrixCreator(dataSet):
    n = len(dataSet)
    pMatrix = [[0.0 for x in range(n)] for y in range(n)]


    for i in range(n):
        x = dataSet[i]
        for j in range(n):
            y = dataSet[j]
            pMatrix[i][j] = x[2]*y[2]*linearKernel(x[:2] ,y[:2])
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




#scalarTest = linearKernel([1,2,3],[1,2,3])
#print(scalarTest)

def generateData():
    classA=[(random.normalvariate(-1.5 ,1),
    random.normalvariate(0.5 ,1),
    1.0)
    for i in range(5)] + \
    [(random.normalvariate(1.5 ,1),
    random.normalvariate(0.5 ,1),
    1.0)
    for i in range(5)]


    classB=[(random.normalvariate(0.0 ,0.5),
    random.normalvariate(-0.5 ,0.5),
    -1.0) for i in range(10)]

    data = classA + classB
    random.shuffle(data)

    return data


'''
pylab.hold(True)
pylab.plot([p[0] for p in classA],
            [p[1] for p in classA],'bo')

pylab.plot([p[0] for p in classB],
            [p[1] for p in classB], 'ro')

pylab.show()

'''

if __name__ == '__main__':
    main()

#data = [(1,-1,1),(1,0,-1)]
#matrix = pMatrixCreator(data)
#print(matrix)


#print(classA)
#print(len(classA))
