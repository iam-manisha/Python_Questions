# wap to create a class called departmental store,create 3 Genric properties and create 4 specific properties and create a admin user as a class method where you can create a (class method like Add product,remove product,sales data,profit and stocks)and create a object method like show items,add items billing and create 1 static method and create 1 object

class departmental_store:
    sname="ABC Store"
    sloc="Banglore"


    def __init__(self,product_name,profit,stock,quantity):
        self.product_name=product_name
        self.profit=profit
        self.stock=stock
        self.quantity=quantity

    
    def display(self):
        print("Name:",self.product_name)
        print("Profit:",self.profit)
        print("Stock:",self.stock)

    @classmethod
    def add_product(cls,name,price,):


