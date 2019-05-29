# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def print_items(self):
        if len(self.inventory) == 0:
            print('[Nothing]\n')
        else: 
            for item in self.inventory:
                print(f"{item.name}: {item.description}")
            print()

    
    
