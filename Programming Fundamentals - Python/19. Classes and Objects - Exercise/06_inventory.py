class Inventory:
    items = []

    def __init__(self, __capacity):
        self.__capacity = __capacity

    def add_item(self, item):
        if len(Inventory.items) < self.__capacity:
            Inventory.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        left_capacity = self.__capacity - len(Inventory.items)
        return f"Items: {', '.join(Inventory.items)}.\nCapacity left: {left_capacity}"


