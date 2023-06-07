class Inventory:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str):
        if len(self.items) == self.__capacity:
            return 'not enough room in the inventory'

        self.items.append(item)

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        items = ', '.join(self.items)
        left_capacity = self.__capacity - len(self.items)
        return f'Items: {items}.\nCapacity left: {left_capacity}'


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)