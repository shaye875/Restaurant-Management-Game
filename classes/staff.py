class Staff:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.energy = 100

    def work(self):
        self.energy-=10
        print(f"{self.name} is work")

    def rest(self):
        if self.energy+20 <= 100:
            self.energy+=20

    def is_tried(self):
        if self.energy <= 30:
            return True
        return  False

    def get_info(self):
         str1 = "the name is "+self.name+ " the salsry is "+str(self.salary)+" the energy is "+str(self.energy)
         return str1

