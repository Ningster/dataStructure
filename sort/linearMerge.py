def linearMerge(L1,L2):
    i = 0
    j = 0
    len1 = len(L1)
    len2 = len(L2)
    result = []
    while i<len1 and j < len2:
        if L1[i]>L2[j]:
            result.append(L2[j])
            j = j+1
        else:
            result.append(L1[i])
            i = i+1
    c=i
    len3=len1
    L=L1
    if i>=len1:
        c=j
        len3=len2
        L=L2
    while c<len3:
        result.append(L[c])
        c=c+1
    return result


#L1=[9,19]
#L2=[5,10,18,20]
#print linearMerge(L1,L2)
