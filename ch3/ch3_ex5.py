name=input("enter the name ")

i=0
temp=""

while i<len(name):
    if name[i] not in temp:
        temp+=name[i]
        print(f"{name[i]}={name.count(name[i])} ")
    i+=1

#bhrgav valani