import monkdata as m
import dtree

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

def getSubsets(n):
    MONK = m.monk1 # Hard coded due to assignment specification
    values = m.attributes[n].values
    subsets = []
    for val in values:
        subsets.append(dtree.select(m.monk1, m.attributes[4], val))
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
            print(l[i][j])
            j+=1
        i+=1
    """
    Summing over the information gains given by the attributes in different
    nodes on level two shows that attribute 1 gives the best information gain
    """
    # print(result)
    return

subsets = getSubsets(4)
infoGainOnSubsets(subsets)
