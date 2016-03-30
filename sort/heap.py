#if the data is heapified, it can then use "adjust" to retrieve the 2nd, 3rd...largest element accordingly

def adjust(a,i,n):   #a in a list of data, i is the root, n is the number of the data
    item = a[i]
    j = 2*i
    while j<=n:
        if j<n and a[j]<a[j+1]: #to find the bigger son
            j = j+1
        if item>=a[j]:  #the position for the itme is found
            break
        else:
            a[j/2]=a[j]
            j = 2*j
    a[j/2]=item

def heapify(a,n):  #bottom up
    for i in range(n/2,0,-1):
        adjust(a,i,n)

def HeapSort(a,n):
    heapify(a,n)
    for i in range(n,1,-1):
        Temp = a[i]
        a[i]=a[1]
        a[1]=Temp
        adjust(a,1,i-1)


listA=[0,77,5,20,1,61,11,59,15,48,19]
HeapSort(listA,10)
print listA
