from staff import *

class Chef(Staff):
    def __init__(self,name,salary,specialty):
        super().__init__(name,salary)
        self.specialty = specialty


    def cook_order(self,order):
        if order.status == "pending":
           order.status = "coking"
        else:
            order.status = "ready"
        self.work()

    def work(self):
        if self.energy-15 >=0:
            self.energy-=15


