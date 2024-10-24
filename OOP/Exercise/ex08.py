class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
        
    def remove_item(self, name, quantity):
        if name in self.items:
            if self.items[name] >= quantity:
                self.items[name] -= quantity
                if self.items[name] == 0:
                    print(f'All {name} are gone now!')
            else:
                print(f'Cannot remove {quantity}. Only {self.items[name]} {name} left')
        else:
            print(f'{name} is not in the inventory.')

    def view_inventory(self):
        for name,quantity in self.items.items():
            print(f'{name}: {quantity}')

# Programa Principal

inventory = Inventory()
inventory.add_item('Apples', 10)
inventory.add_item('Banana', 5)
inventory.remove_item('Apples', 10)
inventory.view_inventory()