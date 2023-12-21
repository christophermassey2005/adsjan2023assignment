
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


"""
L1 = [8,6,6,4]
L2 = [10,7,2,1]
L3 = [9,5,2]


print(Merge3Way(L1, L2, L3))

"""

def MergeSort(L):
    if len(L) <= 1:
        return L
    else:
        mid = len(L) // 2
        L1 = MergeSort(L[:mid])
        L2 = MergeSort(L[mid:])
        return Merge(L1, L2)


def Merge3Sort(L):
    """ If L has at most three elements, sort L into
    non-increasing order without recursive calls.
    Otherwise, make three recursive calls on sub-lists
    whose sizes differ by at most 1, and call Merge3Way
    to merge them. In either case, return a list
    that is a sorted version of L """



    if len(L) <= 1:
        return L
    
    #Special case when L has less than 3 elements - but more than 1 (i.e. we wouldn't make a recursive call on a list of two items, or three items.)
    if len(L) == 3:
         return Merge3Way([L[0]], [L[1]], [L[2]])
    
    if len(L) == 2:
         return Merge3Way([L[0]], [L[1]], [])
    
    else:
        one_third = len(L) // 3
        two_third = one_third * 2
        L1 = Merge3Sort(L[:one_third])
        L2 = Merge3Sort(L[one_third:two_third])
        L3 = Merge3Sort(L[two_third:])
        return Merge3Way(L1, L2, L3)
    
L = [5,19,14,13,2,8,5,19,6]
print(Merge3Sort(L))


