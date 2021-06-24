def rev_ele(l):
    rev=[]
    for i in l:
        rev.append(i[::-1])
    return rev

num=["xyz","pqr","abc"]
print(rev_ele(num))