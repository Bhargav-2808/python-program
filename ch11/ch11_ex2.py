def func(l,**kwargs):
    if kwargs.get('rev')==True:
        return[name[::-1].title() for name in l]
    else:
        return[name.title() for name in l]

name=['bhargav','valani']
print(func(name,rev=True))