init -10 python in rentale:
    class BuyItem(renpy.store.Action):
        def __init__(self, item: InventoryItem, amount: int):
            if type(item) != InventoryItem:
                raise RenTaleTypeError(InventoryItem, type(item))
            if type(amount) != int:
                raise RenTaleTypeError(int, type(amount))

            self.item = item
            self.amount = amount


        def __call__(self):
            inventory.item_buy(self.item, self.amount)
            renpy.restart_interaction()

        
        def get_sensitive(self):
            return ((inventory.money - (self.item.cost * self.amount)) >= 0) if self.item.is_stackable else (((inventory.money - self.item.cost) >= 0) and not inventory.contains(self.item))
