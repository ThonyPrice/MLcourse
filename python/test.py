import monkdata as m
import dtree
import drawtree_qt5 as draw
import random

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

def pruneTree(trainSet):
    monktrain, monkval = partition(trainSet, 0.6)
    tree = dtree.buildTree(monktrain, m.attributes)
    treePermutations = dtree.allPruned(tree)

    bestVal = 0

    for treeP in treePermutations:
        treePerformance = dtree.check(treeP, monkval)
        if (treePerformance > bestVal):
            bestTree = treeP
            bestVal = treePerformance
    return bestVal, bestTree, monkval

def bestPruning():
    bestTreeVal = 0
    bestValData = ()
    i = 0

    while True:
        cur_val, cur_tree, monkValData= pruneTree(m.monk1)
        if cur_val > bestTreeVal:
            bestTreeVal = cur_val
            bestTree = cur_tree
            bestValData = monkValData
            i = 0

        i+=1
        if i == 20000:
            break
    print(dtree.check(bestTree, monkValData))
    print(dtree.check(bestTree, m.monk1test))
    draw.drawTree(bestTree)

#subs = getSubsets(m.monk1,4)
#infoGainOnSubsets(subs)
#getLeaves(m.monk1, 4, 0)
#tree = dtree.buildTree(m.monk2, m.attributes)
#print(dtree.check(tree, m.monk2))

#pruneTree(m.monk1,m.monk1test)
bestPruning()
