init -100 python:
    class InventoryItem():
        def __init__(self, name, quantity, isStackable, image = None, description = ""):
            if type(name) != str:
                raise RenTaleTypeError(str, type(name))
            if type(quantity) != int:
                raise RenTaleTypeError(int, type(quantity))
            if type(isStackable) != bool:
                raise RenTaleTypeError(bool, type(isStackable))
            if image is not None and type(image) != str:
                raise RenTaleTypeError((str, type(None)), type(image))
            if type(description) != str:
                raise RenTaleTypeError(str, type(description))

            self.Name = name
            self.Quantity = quantity
            self.IsStackable = isStackable
            self.Image = image
            self.Description = description

            Inventory.Add(self)


        def Receive(self, quantity: int = 1) -> None:
            """
            If 'IsStackable' adds the specified 'quantity' to current
            """
            if type(quantity) != int:
                raise RenTaleTypeError(int, type(quantity))

            if self.IsStackable:
                self.Quantity += quantity


        def Remove(self, quantity: int = 1) -> None:
            """
            If 'IsStackable' removes the specified 'quantity' from current, Limited to 0
            """
            if type(quantity) != int:
                raise RenTaleTypeError(int, type(quantity))

            if self.IsStackable:
                self.Quantity = max(0, self.Quantity - quantity)
