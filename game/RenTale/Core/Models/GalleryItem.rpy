init -100 python: 
    class GalleryItem():
        def __init__(self, name, label, thumbnail, scope = None, isUnlocked = False):
            if type(name) != str:
                raise TypeError(f"Expected 'String', got '{type(name).__name__}'")
            if type(label) != str:
                raise TypeError(f"Expected 'String', got '{type(label).__name__}'")
            if type(thumbnail) != str:
                raise TypeError(f"Expected 'String', got '{type(thumbnail).__name__}'")
            if scope is not None and type(scope) != dict:
                raise TypeError(f"Expected 'Dictionary' or 'None', got '{type(scope).__name__}'")
            if type(isUnlocked) != bool:
                raise TypeError(f"Expected 'Bool', got '{type(isUnlocked).__name__}'")

            self.Name = name
            self.Label = label
            self.Thumbnail = thumbnail
            if scope is None:
                self.Scope = {}
            else:
                self.Scope = scope

            if name not in persistent.RenTale_Gallery:
                persistent.RenTale_Gallery[name] = isUnlocked
                self.IsUnlocked = isUnlocked
            else:
                self.IsUnlocked = persistent.RenTale_Gallery[name]

            RenTale_Gallery_List.add(self)

        
        def Unlock(self) -> None:
            if not self.IsUnlocked:
                self.IsUnlocked = True
                persistent.RenTale_Gallery[self.Name] = True
