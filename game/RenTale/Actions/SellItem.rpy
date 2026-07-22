init -10 python in rentale:
    class SellItem(renpy.store.Action):
        def __init__(self, item: InventoryItem, amount: int):
            if type(item) != InventoryItem:
                raise RenTaleTypeError(InventoryItem, type(item))
            if type(amount) != int:
                raise RenTaleTypeError(int, type(amount))

            self.item = item
            self.amount = amount


        def __call__(self):
            inventory.item_sell(self.item, self.amount)
            renpy.restart_interaction()

        
        def get_sensitive(self):
            return inventory.contains(self.item) and self.item.quantity >= self.amount
