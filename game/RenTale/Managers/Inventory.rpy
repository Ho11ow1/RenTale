init -90 python in rentale:
    class Inventory():
        def __init__(self):
            self.money = 0
            self.items = list()

# ============================== BASIC ============================== #
        def add(self, item: InventoryItem, quantity: int | None = None) -> None:
            if type(item) != InventoryItem:
                raise RenTaleTypeError(InventoryItem, type(item))

            if item not in self.items:
                self.items.append(item)
                if item.is_stackable:
                    if quantity is not None and quantity > 1:
                        item.quantity = quantity
                    else:
                        item.quantity = 1
                else:
                    item.quantity = 1


        def remove(self, item: InventoryItem) -> None:
            if type(item) != InventoryItem:
                raise RenTaleTypeError(InventoryItem, type(item))

            if item in self.items:
                self.items.remove(item)
                item.quantity = 0

        
        def contains(self, item: InventoryItem) -> bool:
            if type(item) != InventoryItem:
                raise RenTaleTypeError(InventoryItem, type(item))

            return item in self.items

# ============================== MONEY ============================== #
        def money_set(self, amount: int) -> None:
            if type(amount) != int:
                raise RenTaleTypeError(int, type(amount))

            self.money = max(0, amount)


        def money_gain(self, amount: int) -> None:
            if type(amount) != int:
                raise RenTaleTypeError(int, type(amount))

            self.money += amount


        def money_lose(self, amount: int) -> None:
            if type(amount) != int:
                raise RenTaleTypeError(int, type(amount))

            self.money = max(0, self.money - amount)

# ============================== ITEMS ============================== #
        def item_set_quantity(self, item: InventoryItem, quantity: int) -> None:
            if type(item) != InventoryItem:
                raise RenTaleTypeError(InventoryItem, type(item))
            if type(quantity) != int:
                raise RenTaleTypeError(int, type(quantity))

            if item not in self.items:
                self.add(item, max(1, quantity))
            else:
                item.quantity = max(1, quantity)


        def item_gain(self, item: InventoryItem, quantity: int) -> None:
            if type(item) != InventoryItem:
                raise RenTaleTypeError(InventoryItem, type(item))
            if type(quantity) != int:
                raise RenTaleTypeError(int, type(quantity))

            if item not in self.items:
                self.add(item, quantity)
            else:
                if item.is_stackable:
                    item.quantity += quantity


        def item_lose(self, item: InventoryItem, quantity: int) -> None:
            if type(item) != InventoryItem:
                raise RenTaleTypeError(InventoryItem, type(item))
            if type(quantity) != int:
                raise RenTaleTypeError(int, type(quantity))

            if item in self.items:
                if item.quantity - quantity <= 0:
                    self.remove(item)
                else:
                    item.quantity -= quantity

# ============================== BUY / SELL ============================== #
        def item_buy(self, item: InventoryItem, quantity: int) -> bool:
            if type(item) != InventoryItem:
                raise RenTaleTypeError(InventoryItem, type(item))
            if type(quantity) != int:
                raise RenTaleTypeError(int, type(quantity))

            cost = item.cost * (quantity if item.is_stackable else 1)
            if self.money < cost:
                return False
            if not item.is_stackable and item in self.items:
                return False

            self.money_lose(cost)
            self.item_gain(item, quantity)
            return True


        def item_sell(self, item: InventoryItem, quantity: int) -> None:
            if type(item) != InventoryItem:
                raise RenTaleTypeError(InventoryItem, type(item))
            if type(quantity) != int:
                raise RenTaleTypeError(int, type(quantity))
            if item in self.items and quantity > item.quantity:
                raise RenTaleArgumentException(f"Given quantity: '{quantity}' is greater than the items current quantity: '{item.quantity}'")

            if item in self.items:
                gain_amount = item.cost * (quantity if item.is_stackable else 1)
                self.money_gain(gain_amount)
                self.item_lose(item, quantity)
