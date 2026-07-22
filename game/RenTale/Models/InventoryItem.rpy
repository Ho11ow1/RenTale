init -100 python in rentale:
    class InventoryItem():
        def __init__(self, name: str, is_stackable: bool = False, image: str | None = None, description: str = "", cost: int = 0):
            """
            Represents an inventory item. Automatically registers into Inventory on creation.
            """
            if type(name) != str:
                raise RenTaleTypeError(str, type(name))
            if type(is_stackable) != bool:
                raise RenTaleTypeError(bool, type(is_stackable))
            if image is not None and type(image) != str:
                raise RenTaleTypeError((str, type(None)), type(image))
            if type(description) != str:
                raise RenTaleTypeError(str, type(description))

            self.name = name
            self.quantity = 0
            self.is_stackable = is_stackable
            self.image = image
            self.description = description
            self.cost = cost

            all_items.add(self)
