def dev(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('can not devide by zero')
    except TypeError as err:
        print(err)
    except :
        print("not valid input")
