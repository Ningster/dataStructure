def partition(a,i,j):
    pivot = a[i]
    m = i  #will need the original i later
    while m<j:
        while m<=j and a[m]<=pivot:
            m = m+1
        while j>=m and a[j]>=pivot:
            j = j-1
        if m<j:
            temp = a[m]
            a[m]=a[j]
            a[j]=temp
    a[i]=a[j]
    a[j]=pivot
    return j

def QuickSort(a,p,q):
    if p<q:
        j = partition(a,p,q)
        QuickSort(a,p,j-1)
        QuickSort(a,j+1,q)
    else:
        pass
#listA=[5,3,8,4,9]
#listA=[4,3,5,8,9]
#listA=[1,2,3,4]
#listA = [54,26,93,17,77,31,44,55,20]
listA=[3,3]
QuickSort(listA,0,1)
print listA
