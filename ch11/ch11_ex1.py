def power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "not entered"

nums=[1,2,3]
print(power(2,*nums))