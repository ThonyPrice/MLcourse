import monkdata as m
import dtree
import drawtree_qt5 as draw

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

getLeaves(m.monk1, 4, 0)
draw.drawTree(dtree.buildTree(m.monk1, m.attributes, 2))

#subsets = getSubsets(m.monk1, 4)
#infoGainOnSubsets(subsets)
'''
for att in att5

    for att in att1

x = dtree.select(m.monk1, m.attributes[4], 1)
y = dtree.select(x, m.attributes[4], 3)
z = dtree.mostCommon(y)
print(z)
'''
