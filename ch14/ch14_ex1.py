from functools import wraps
import time

def calculate_time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        t1= time.time()
        value=func(*args,**kwargs)
        t2= time.time()
        total_time=t2-t1
        print(f"it takes tool {total_time} second")
        return value
    return wrapper

@calculate_time
def square(n):
    return[i**2 for i in range(1,n+1)]

print(square(100))