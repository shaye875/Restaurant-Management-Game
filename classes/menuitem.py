class Menuitem:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
        self.__available = True

    def get_info(self):
        print(f"the name is {self.name} the price is {self.price} the category is {self.category} and is available: {self.__available}")

    def set_available(self,status):
        self.__available = status

    def is_available(self):
        print(self.__available)


