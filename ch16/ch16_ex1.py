class laptop:
    def __init__(self,brand_name,ssd,price):
        self.brand=brand_name
        self.ssd=ssd
        self.price=price

laptop1=laptop('dell','256gb',55000)
laptop2=laptop('hp','512gb',60000)
print(laptop1.price)