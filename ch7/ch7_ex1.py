def cube(l):
    c={}
    for i in range(1,l+1):
        c[i]=i**3
    return c

print(cube(8))