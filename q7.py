"""
def Merge(L1, L2):
    L = []
    while L1 and L2:
        if L1[0] <= L2[0]:
            L.append(L1.pop(0))
        else:
            L.append(L2.pop(0))
    L.extend(L1)
    L.extend(L2)
    return L
"""

def Merge3Way(L1,L2, L3):
    """ Merge the three lists L1, L2, L3 that are sorted
    in non-increasing order into a new list L that is
    sorted in non-increasing order, and return L """

    def Merge2Way(List1, List2):
        L = []
        while List1 and List2:
            if List1[0] >= List2[0]:    #Sign changed, as in reverse order
                L.append(List1.pop(0))
            else:
                L.append(List2.pop(0))
        L.extend(List1)
        L.extend(List2)
        return L
    
    twomerged = Merge2Way(L1, L2)
    threemerged = Merge2Way(twomerged, L3)
    return threemerged
        
    #Naive implementation - merge the first two lists, then the third. - Not the most efficient!



L1 = [8,6,6,4]
L2 = [10,7,2,1]
L3 = [9,5,2]


print(Merge3Way(L1, L2, L3))




