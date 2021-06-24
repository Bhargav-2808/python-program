user={}
name=input("enter the name: ")
age=input("enter the age: ")
movie=input("enter fav movies comma saperatly :").split(",")
song=input("enter favourite song :").split(",")

user['name']=name
user['age']=age
user['movie']=movie
user['song']=song
for key, value in user.items():
    print(f"{key} : {value} ")
