class person:
    count=0
    
    def __init__(self,fname,lname,age):

        person.count+=1
        self.fname=fname
        self.lname=lname
        self.age=age
p1=person('bhargav','valani',18)
print(person.count)