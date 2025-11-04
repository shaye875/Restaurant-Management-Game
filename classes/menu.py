class Menu:
    items = []
    def add_item(self,item):
        self.items.append(item)

    def remove_item(self,name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)

    def get_item_by_name(self,name):
        for item in self.items:
            if item.name == name:
                return item

    def get_item_by_category(self,category):
        for item in self.items:
            if item.category == category:
                return item

    def display_manu(self):
        str = ""
        i = 1
        for item in self.items:
            print(i)
            item.get_info()
            i+=1

    def get_total_items(self):
        return len(self.items)


