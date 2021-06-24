def comm(l1,l2):
    l3=[]
    for i in l1:
        if i in l2:

            l3.append(i)
    return l3


print(comm([1,2,3,4],[1,2,6,7]))
            