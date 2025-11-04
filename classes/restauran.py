from classes.menu import *


from classes.waiter import *

class Restaurant:
    def __init__(self,name):
        self.name = name
        self.menu =  Menu
        self.staff = []
        self.orders = []
        self.money = 1000

    def hire_staff(self,staff_number):
        self.staff.append(staff_number)

    def fire_staff(self,stafe_name):
        for staff1 in self.staff:
            if staff1.name == stafe_name:
                self.staff.remove(staff1)

    def create_order(self,customer,waiter,menu,num):
        self.orders.append(waiter.take_order(customer,menu,num))

    def complete_order(self,order):
        self.money+=order.get_total()


    def pay_salaries(self):
        for staff in self.staff:
            self.money-=staff.salary

    def get_statistics(self):
        return {"sum of orders is":{len(self.orders)},"num of money is":{self.money},"num of staff is":{len(self.staff)}}

    def display_status(self):
        str =  "name is: "+self.name+ " staff is :"
        for staff in self.staff:
            str+=staff.get_info()
        str += " oders is: "
        for order in self.orders:
            str+=order.display_order()
        return str
