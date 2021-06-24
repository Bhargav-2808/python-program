#def rev(l):
#   l.reverse()
#   return l
#num=[1,2,3,4]
#print(rev(num))

#def rev(l):
#   return l[::-1]
#num=[1,2,3,4]
#print(rev(num))

  
def rev(l):
    re=[]
    for i in range(len(l)) :
        popped=l.pop()
        re.append(popped)
    return re                                             # or(1.len(l)+1)

num=[1,2,3,4,5]
print(rev(num))