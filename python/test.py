import monkdata as m
import dtree
import drawtree_qt5 as draw
import random
import matplotlib.pyplot as plt
import statistics

monks = [m.monk1, m.monk2, m.monk3]

def monkEntropyAndInfoGain(monks):
    i = 0
    while (i < len(monks)):
        print("Entropy of dataset for Monk-" + str(i+1) + " = "
            + str(dtree.entropy(monks[i])))
        j = 0
        while (j < len(m.attributes)):
            print("For Monk-" + str(i+1) +". Information gain on attribute "
                + str(j+1) + " = " + str(dtree.entropy(monks[i])))
            j+=1
        i+=1
        print("\n")
    return

def getSubsets(set, n):
    values = m.attributes[n].values
    subsets = []
    for val in values:
        subsets.append(dtree.select(m.monk1, m.attributes[4], val))
        # print(dtree.select(m.monk1, m.attributes[4], val))
    return subsets

def infoGainOnSubsets(subsets):
    l = []  # List containing subsets depending on what choice was made
            # in previous node
    for sset in subsets:
        attribute_gains = []
        j = 0
        while (j < len(m.attributes)):
            attribute_gains.append(dtree.averageGain(sset, m.attributes[j]))
            j+=1
        l.append(attribute_gains)
    result = [0] * len(m.attributes)
    i = 0
    while i < len(l):
        j = 0
        while j < len(m.attributes):
            result[j] += (l[i][j])
            #print((l[i][j]))
            j+=1
        i+=1
    """
    Summing over the information gains given by the attributes in different
    nodes on level two shows that attribute 1 gives the best information gain
    """
    print(result)
    return

def getLeaves(dataSet, a1, a2):
    a1_domain = m.attributes[a1].values
    a2_domain = m.attributes[a2].values

    for k in a1_domain:
        x = dtree.select(dataSet, m.attributes[a1], k)
        for l in a2_domain:
            y = dtree.select(x, m.attributes[a2], l)
            z = dtree.mostCommon(y)
            print("For " + str(k) + ":" + str(l) + ", " + "most common = " + str(z))

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

def pruneTree(trainSet, fraction):
    monktrain, monkval = partition(trainSet, fraction)
    bestTree = dtree.buildTree(monktrain, m.attributes)
    treePermutations = dtree.allPruned(bestTree)


    bestVal = dtree.check(bestTree, monkval)

    for treeP in treePermutations:
        treePerformance = dtree.check(treeP, monkval)
        if (treePerformance > bestVal):
            bestTree = treeP
            bestVal = treePerformance
    return bestVal, bestTree, monkval

def bestPruning(data, fraction, iterations, dataTest):
    bestTreeVal = 0
    bestValData = ()
    allData = [0]*iterations
    i = 0

    while True:
        cur_val, cur_tree, monkValData= pruneTree(data, fraction)
        allData[i] = (dtree.check(cur_tree,dataTest))
        if cur_val > bestTreeVal:
            bestTreeVal = cur_val
            bestTree = cur_tree
            bestValData = monkValData
            #i = 0

        i+=1
        if i == iterations:
            break
    #print(dtree.check(bestTree, monkValData))
    #print(dtree.check(bestTree, m.monk1test))
    #print("Mean: " + str(statistics.mean(allData)))
    #print("Standard Deviation: " + str(statistics.stdev(allData)))
    #print(allData)
    return statistics.mean(allData), statistics.stdev(allData)
    #draw.drawTree(bestTree)

#subs = getSubsets(m.monk1,4)
#infoGainOnSubsets(subs)
#getLeaves(m.monk1, 4, 0)
#tree = dtree.buildTree(m.monk1, m.attributes, 2)
#draw.drawTree(tree)
#print(dtree.check(tree, m.monk2))
#tree = dtree.buildTree(m.monk3, m.attributes)
#print(dtree.check(tree, m.monk3test))
#pruneTree(m.monk1,m.monk1test)
fractions = [0.3,0.4,0.5,0.6,0.7,0.8]
iterations = 10000
xAxis = []
errorAxis = []

for frac in fractions:
    mean, stdev = bestPruning(m.monk3, frac, iterations, m.monk3test)
    xAxis.append(mean)
    errorAxis.append(stdev)

#print(xAxis)
#print(errorAxis)

lb = "Mean of optimal pruning from " + str(iterations) + " splits with one standard deviation"
plt.errorbar(fractions, xAxis, errorAxis, lineStyle='-', marker='*', label=lb, mew=5, capsize= 5, capthick=1)
plt.ylabel('Accuracy towards testingdata', fontsize=20)
plt.xlabel('Fraction of training data split', fontsize=20)
plt.legend(loc='lower right',prop={'size': 20})
plt.grid(True)
plt.title("Monk3", fontsize=30)
plt.axis([0.2,0.9,0.6,1])

plt.show()
