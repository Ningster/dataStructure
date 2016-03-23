def SelSort(my_list):
    for i in range(0, len(my_list)-1):
        minTemp = my_list[i]
        minIndex = i
        for j in range(i+1,len(my_list)):  # the time complexity of the second loop is n-1, n-2, n-3....1
            if minTemp > my_list[j]:
                minTemp = my_list[j]
                minIndex = j
        my_list[minIndex] = my_list[i]
        my_list[i]=minTemp
    return my_list

listA = [47,12,86,94,56,32,71,85,88,92]
print SelSort(listA)
