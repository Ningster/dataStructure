from linearMerge import linearMerge


def mergeSort(a):
    result = []
    n = len(a)
    if n==1:
        result = result + a
    else:
        aList = mergeSort(a[0:n/2])
        bList = mergeSort(a[n/2:n])
        result = linearMerge(aList, bList)
    return result


a=[310,285,179,652,351,423,861,254,450,520]
print mergeSort(a)
