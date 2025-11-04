from  classes.staff import *
from classes.order import *


class Waiter(Staff):
    def __init__(self,name,salary):
        super().__init__(name,salary)
        self.typs = 0

    def take_order(self,customer,menu,num):
        order = Order(customer,num)
        while True:
          menu.display_manu()
          item1 = input("which item do you want")

          order.add_item(menu.get_item_by_name(item1))
          exit = input("if you want exit print exit else print sumthing")
          if exit == "exit":
              break
        return order

    def serve_order(self,order):
        order.set_status("delivered")
        order.customer.is_happy()

    def receive_tip(self,num):
        self.typs+=num

    def get_total_earnings(self):
        return self.salary+self.typs



