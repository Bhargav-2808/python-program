weight=int(input("Enter the weight in pound or kilogram  "))
unit=input("enter weight in (L)bs or (K)g  ")
if unit.upper()=="L":
    convert=weight*0.45
    print(f"you are {convert} kilos")
else:
    convert=weight/0.45
    print(f"you are {convert} pound")