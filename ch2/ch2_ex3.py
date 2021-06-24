name,char=input("enter the name and character with comma saperated : ").split(",")

print(f"lenght of your name is :{len(name)}  ")
print(f"character of your name is :{name.lower().count(char.lower())} ") # case sensitive