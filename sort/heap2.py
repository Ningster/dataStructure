def heapify(a,i,n): #time complexity of comparison is n/2
    j = 2*i  #left child of i
    if i>n : #if no i
        return 0
    elif j>n : #if no child
        return a[i]
    else: #if has child
        if heapify(a,j,n)>heapify(a,j+1,n):  # to find the larger child
            pass
        else:
            j = j+1
        if a[j] > a[i]:  # if the child is larger than self, swap
            temp = a[i]
            a[i]=a[j]
            a[j]=temp
            return a[i]
        else:
            return a[i]

def heapsort(a,n): #time complexity is nxn
    for i in range(n,1,-1):
        heapify(a,1,i)
        temp = a[1]
        a[1]=a[i]
        a[i]=temp

listA=[0,15,5,20,1,61,11,59,77,48,19]


#heapsort(listA,10)
#print listA
print heapify(listA,1,10)
print listA
