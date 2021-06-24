class laptop:
    def __init__(self,brand_name,ssd,price):
        self.brand=brand_name
        self.ssd=ssd
        self.price=price

    def disc(self,num):
        off=(num/100)*(self.price)
        return self.price-off

laptop1=laptop('dell','256gb',55000)
laptop2=laptop('hp','512gb',60000)


print(laptop2.disc(10))