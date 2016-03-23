def down(my_list, f, t):
    while t >= f:
        if my_list[t+1]==None:
            my_list[t+1]=my_list[t]
            my_list[t]=None
            t = t-1

def InsSort(my_list):
    for i in range(0,len(my_list)-1):
        if my_list[i+1] > my_list[i]:
            pass   #sorted list, the time complexity in the best case is n (pass every time after comparison)
        else:
            for j in range(0,i+1):  #sorted list, the time complexity in the worth case is 1,2,3.....n-1
                while my_list[i+1] < my_list[j]:
                    temp = my_list[i+1]
                    my_list[i+1]=None
                    down(my_list,j,i)
                    my_list[j]=temp
                    break
    return my_list

listA=[5,8,3,2,9]
listB = [47,12,20,2,48,6,71,5,88,3]
listC = [12,20,2,48,6,71,5,88,3]
listC = [3,2,1,45,67,23,9,8,7]
print InsSort(listC)
