class Customer:
    def __init__(self,name):
        self.name = name
        self.__satisfaction = 50

    def increase_satisfaction(self,amount):
        if amount+self.__satisfaction <= 100:
            self.__satisfaction += amount

    def decrease_satisfaction(self,amount):
        if self.__satisfaction-amount >= 0:
            self.__satisfaction-=amount

    def is_happy(self):
        if self.__satisfaction >= 70:
            return True
        else:
            return False

    def get_info(self):
        print(f"the name of customer is {self.name} the satisfaction for him is {self.__satisfaction}")

