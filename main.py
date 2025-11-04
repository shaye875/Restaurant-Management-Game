from classes.restauran import *
from classes.customer import *
from classes.waiter import *
from classes.menuitem import *
from classes.menu import *
res = Restaurant("shaye")
costomer = Customer("avi")
menuitwm1 = Menuitem("mit",50,"mit")
waiter1 = Waiter("kobi",5000)
res.hire_staff(waiter1)
menu =  Menu()
menu.add_item(menuitwm1)
res.create_order(costomer,waiter1,menu)
print(res.display_status())
