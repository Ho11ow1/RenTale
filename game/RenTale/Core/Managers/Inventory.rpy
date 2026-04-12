init -90 python:
    class RenTale_Inventory():
        def __init__(self):
            self.Items = set()


        def Add(self, item: InventoryItem) -> None:
            if type(item) != InventoryItem:
                raise RenTaleTypeError(InventoryItem, type(item))

            self.Items.add(item)


        def Remove(self, item: InventoryItem) -> None:
            if type(item) != InventoryItem:
                raise RenTaleTypeError(InventoryItem, type(item))

            if item in self.Items:
                self.Items.remove(item)


        def Contains(self, item: InventoryItem) -> bool:
            if type(item) != InventoryItem:
                raise RenTaleTypeError(InventoryItem, type(item))

            return item in self.Items
