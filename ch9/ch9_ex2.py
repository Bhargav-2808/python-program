def sr(l):
    return [str(name) for name in l if (type(name)== int or type(name)==float)]

print(sr([1.0,1,2,"bhar",[1,2,3],(2,3)]))