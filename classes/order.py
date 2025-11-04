class Order:
    def __init__(self,customer,order_number):
        self.customer = customer
        self.order_number = order_number
        self.items = []
        self.status = "pending"
        self.total_price = 0

    def add_item(self,item):
        self.items.append(item)
        self.total_price+=item.price

    def remove_item(self,item):
        for item1 in self.items:
            if item1.name == item.name:
               self.items.remove(item1)
               self.total_price-=item.price

    def get_total(self):
        return self.total_price

    def set_status(self,status):
        self.status = status

    def display_order(self):
        str1 = "the number of order is"+ self.order_number+" the customer is "+self.customer.name+" the menuitem is:"
        for item in self.items:
            str1 += item.name
        str1 +="total price:"
        str1+=str(self.total_price)
        str1+="tje status is "+self.status
        return str1

    def is_complete(self):
        if self.status == "delivered":
            return True
        return False

