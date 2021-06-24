def even(num):
    for nums in range(2,num+1,2):
        yield(nums)

evens=even(10)

for num in evens:
    print(num)
