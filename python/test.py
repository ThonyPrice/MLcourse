import monkdata as m
import dtree



print("Entropy for dataset monk1 : " + str(dtree.entropy(m.monk1)))
i = 0

while (i<6):
    print("Information gain for attribute " + str(i+1) + " : " + str(dtree.averageGain(m.monk1, m.attributes[i])))
    i+=1

print("\n")


print("Entropy for dataset monk2 : " + str(dtree.entropy(m.monk2)))
i = 0

while (i<6):
    print("Information gain for attribute " + str(i+1) + " : " + str(dtree.averageGain(m.monk2, m.attributes[i])))
    i+=1

    
print("\n")


print("Entropy for dataset monk3 : " + str(dtree.entropy(m.monk3)))
i = 0

while (i<6):
    print("Information gain for attribute " + str(i+1) + " : " + str(dtree.averageGain(m.monk3, m.attributes[i])))
    i+=1
