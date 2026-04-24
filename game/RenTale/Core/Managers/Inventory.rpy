init -90 python:
    class RenTale_Inventory():
        def __init__(self):
            self.Items = set()


        def Add(self, item: InventoryItem) -> None:
            """
            Adds the given 'item' to the inventory if it not already in the inventory
            """
            if type(item) != InventoryItem:
                raise RenTaleTypeError(InventoryItem, type(item))

            if item not in self.Items:
                self.Items.add(item)


        def Remove(self, item: InventoryItem) -> None:
            """
            Removes the given 'item' if it is found in the inventory
            """
            if type(item) != InventoryItem:
                raise RenTaleTypeError(InventoryItem, type(item))

            if item in self.Items:
                self.Items.remove(item)


        def Contains(self, item: InventoryItem) -> bool:
            """
            Returns true if the given 'item' is found in the inventory
            """
            if type(item) != InventoryItem:
                raise RenTaleTypeError(InventoryItem, type(item))

            return item in self.Items
