import dtree
# import drawtree_qt5 as draw
import monkdata as m
from pylab import *
import random

def monkEntropyAndInfoGain(monks):
    """
    Print Entropy of all MONK datasets and information gain on each
    of their attributes.
    """
    i = 0
    while (i < len(monks)):
        print("Entropy of dataset for Monk-" + str(i+1) + " = "
            + str(dtree.entropy(monks[i])))
        j = 0
        while (j < len(m.attributes)):
            print("For Monk-" + str(i+1) +". Information gain on attribute "
                + str(j+1) + " = " + str(dtree.averageGain(monks[i], m.attributes[j])))
            j+=1
        i+=1
        print("\n")
    return

def getSubsets(set, n):
    """
    Return a list of all subsets from a set split on attribute n
    """
    values = m.attributes[n].values
    subsets = []
    for val in values:
        subsets.append(dtree.select(m.monk1, m.attributes[4], val))
    return subsets

def infoGainOnSubsets(subsets):
    """
    Print information gain on all attributes of all subsets in argument
    """
    l = []  # List of subsets
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
            print("Gain on branch [" + str(i) + " - " + str(j) + "] = " + str(l[i][j]))
            j+=1
        i+=1
        print("\n")
    return

def getLeaves(dataSet, a1, a2):
    """
    Print most common (T/F) in leaves of dataSet split on a1 then a2
    """
    a1_domain = m.attributes[a1].values
    a2_domain = m.attributes[a2].values
    for k in a1_domain:
        x = dtree.select(dataSet, m.attributes[a1], k)
        for l in a2_domain:
            y = dtree.select(x, m.attributes[a2], l)
            z = dtree.mostCommon(y)
            print("For " + str(k) + ":" + str(l) + ", " + "most common = " + str(z))

def partition(data, fraction):
    """
    Given a dataset, randomly split it into a traning set and
    a validation set, return both of them
    """
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

def pruneTree(data, attributes, fraction):
    """
    Return fraction of correctly classified samples from the best tree
    from dataSet given a fraction
    """
    trainingdata, validationdata = partition(data, fraction)
    tree = dtree.buildTree(trainingdata, attributes)
    besttree = bestPruning(tree, validationdata)
    return dtree.check(besttree, validationdata)

def bestPruning(tree, validationdata):
    """
    Given a tree and validationdata return the pruned tree that
    has the best performance against the validation data
    """
    all_pruned_trees = dtree.allPruned(tree)
    besttree = tree
    bestperformance = dtree.check(besttree, validationdata)
    for candidatetree in all_pruned_trees:
        candidateperformance = dtree.check(candidatetree, validationdata)
        if (candidateperformance > bestperformance):
            besttree = candidatetree
            bestperformance = candidateperformance
    if besttree == tree:
        return tree
    else:
        return bestPruning(besttree, validationdata)

def a7():
    fractions = [.3, .4, .5, .6, .7, .8]
    monk1_error = []
    monk3_error = []
    tries = 1000
    for fraction in fractions:
        for dataset in [m.monk1, m.monk3]:
            value = 0.0
            for i in range(0, tries):
                value += pruneTree(dataset, m.attributes, fraction)
            value = round((value/tries), 6)
            if dataset == m.monk1:
                monk1_error.append(value)
            else:
                monk3_error.append(value)

    print("Errors for fractions")
    print(fractions)
    print(monk1_error)
    print(monk3_error)
    title('Mean val of correction')
    xlabel('Fraction for test- and validationdata')
    ylabel('Correct classification rate')
    grid(True)
    plot(fractions, monk1_error, '-r',
        fractions, monk3_error, '-b')
    show()

def main():
    monks = [m.monk1, m.monk2, m.monk3]
    monkEntropyAndInfoGain(monks)
    subs = getSubsets(m.monk1, 4)
    infoGainOnSubsets(subs)
    a7()

if __name__ == "__main__":
    main()
