def swap(my_list, i, j):
    temp = my_list[i]
    my_list[i]=my_list[j]
    my_list[j]=temp
    return my_list

def QSort(my_list):
    n = len(my_list)
    pivot = my_list[0]
    newList = []
    big = None
    small = None
    if n == 1:              #termination condition
        newList = my_list
    else:
        for i in range(1,n):
            if my_list[i]>pivot:
                big = i
                break
        for j in range(n-1,0,-1):
            if my_list[j]<pivot:
                small = j
                break
        if big is None:
            my_list = swap(my_list,0,n-1)
            newList = QSort(my_list[0:n-1])+[my_list[n-1]]
        elif small is None:
            newList = [my_list[0]]+QSort(my_list[1:n])
        else:
            if i < j:
                my_list = swap(my_list,i,j)
                newList = QSort(my_list)
            else:
                my_list = swap(my_list,0,j)
                newList = QSort(my_list[0:j])+[my_list[j]]+QSort(my_list[j+1:n])
    return newList

listA = [54,26,93,17,77,31,44,55,20]
print QSort(listA)
