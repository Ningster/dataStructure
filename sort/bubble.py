def swap(my_list, n):
    if my_list[n]>my_list[n+1]:
        temp = my_list[n+1]
        my_list[n+1]=my_list[n]
        my_list[n]=temp


def BubSort(my_list):
    for n in range(0,len(my_list)-1):
        x = 0
        while x < len(my_list)-(n+1) : # the time complexity of the second loop is n-1, n-2, n-3....1
            swap(my_list,x)
            x = x+1
    return my_list


listA = [8,7,6,5,4]
print BubSort(listA)

print listA
