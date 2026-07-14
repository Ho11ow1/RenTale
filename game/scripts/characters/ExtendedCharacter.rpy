init -100 python:
    from enum import Enum

    class StatType(Enum):
        Friendship = 0
        Love = 1
        Lust = 2


init -100 python:
    class ExtendedCharacter(renpy.character.ADVCharacter):
        def __init__(self, name, note = "", relationship = "", **properties):
            # Init actual character
            super().__init__(name, **properties)
            # Custom stats
            self.Friendship = 0
            self.Love = 0
            self.Lust = 0
            # Small character note for a bio / card note
            self.Note = note
            # Specific relation to player
            self.Relationship = relationship

            rentale.all_characters.add(self)


        def increase_stat(self, stat: StatType, amount: int) -> None:
            if type(stat) != StatType:
                raise rentale.RenTaleTypeError(StatType, type(stat))
            if type(amount) != int:
                raise rentale.RenTaleTypeError(int, type(amount))
            
            match stat:
                case StatType.Friendship:
                    self.Friendship += amount
                case StatType.Love:
                    self.Love += amount
                case StatType.Lust:
                    self.Lust += amount


        def decrease_stat(self, stat: StatType, amount: int) -> None:
            if type(stat) != StatType:
                raise rentale.RenTaleTypeError(StatType, type(stat))
            if type(amount) != int:
                raise rentale.RenTaleTypeError(int, type(amount))

            match stat:
                case StatType.Friendship:
                    self.Friendship -= amount
                case StatType.Love:
                    self.Love -= amount
                case StatType.Lust:
                    self.Lust -= amount


        def change_relationship(self, relationship: str) -> None:
            if type(relationship) != str:
                raise rentale.RenTaleTypeError(str, type(relationship))
            
            self.Relationship = relationship

        
        def change_note(self, note: str) -> None:
            if type(note) != str:
                raise rentale.RenTaleTypeError(str, type(note))

            self.Note = note


# ============================== DYNAMIC MODIFICATION METHODS | PARTIAL ONLY ============================== #
        @property
        def Name(self) -> str:
            return self.name

        @Name.setter
        def Name(self, value) -> None:
            self.name = value


        @property
        def Color(self) -> str:
            val = self.who_args.get("color")
            return val if val is not None else renpy.gui.text_color

        @Color.setter
        def Color(self, value) -> None:
            self.who_args["color"] = value


        @property
        def WhatColor(self) -> str:
            val = self.what_args.get("color")
            return val if val is not None else renpy.gui.text_color

        @WhatColor.setter
        def WhatColor(self, value) -> None:
            self.what_args["color"] = value
