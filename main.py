from classes.restauran import *
from classes.customer import *
from classes.waiter import *
from classes.menuitem import *
from classes.menu import *
def show_menu():
    chois = input("1-get order 2-shwo in the orders 3-show the statics 4-end")
    return chois
def run_day(res,costomer,waiter,menu):
  num = 0
  while True:
   num+=1
   try:
    choish = show_menu()
    if choish == "1":
        res.create_order(costomer,waiter,menu,num)

        res.complete_order(res.orders[-1])
    elif choish =="2":
        print(res.display_status())
    elif choish == "3":
        print(res.get_statistics())
    elif choish == "4":

        print(res.display_status())
        break
   except:
       print("try agein")

def play(res,costomer,waiter,menu):
    while True:
        run_day(res,costumer,waiter,menu)
        exit = input("if you want to exit enter exit")
        if exit == "exit":
            break
costumer = Customer("avi")
waiter = Waiter("kobi",2000)
mit = Menuitem("mit",15,"mit")
fish = Menuitem("fish",50,"mit")
menu = Menu()
menu.add_item(mit)
menu.add_item(fish)
res = Restaurant("goldis")
res.hire_staff(waiter)
if __name__ == "__main__":
    play(res,costumer,waiter,menu)