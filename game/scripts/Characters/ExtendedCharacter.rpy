init -100 python:
    from enum import Enum

    class StatType(Enum):
        friendship = 0
        love = 1
        lust = 2


init -100 python:
    class ExtendedCharacter(renpy.character.ADVCharacter):
        def __init__(self, name, note = "", relationship = "", **properties):
            # Init actual character
            super().__init__(name, **properties)
            # Custom stats
            self.friendship = 0
            self.love = 0
            self.lust = 0
            # Small character note for a bio / card note
            self.note = note
            # Specific relation to player
            self.relationship = relationship

            rentale.all_characters.add(self)


        def increase_stat(self, stat: StatType, amount: int) -> None:
            if type(stat) != StatType:
                raise rentale.RenTaleTypeError(StatType, type(stat))
            if type(amount) != int:
                raise rentale.RenTaleTypeError(int, type(amount))
            
            match stat:
                case StatType.friendship:
                    self.friendship += amount
                case StatType.love:
                    self.love += amount
                case StatType.lust:
                    self.lust += amount


        def decrease_stat(self, stat: StatType, amount: int) -> None:
            if type(stat) != StatType:
                raise rentale.RenTaleTypeError(StatType, type(stat))
            if type(amount) != int:
                raise rentale.RenTaleTypeError(int, type(amount))

            match stat:
                case StatType.friendship:
                    self.friendship -= amount
                case StatType.love:
                    self.love -= amount
                case StatType.lust:
                    self.lust -= amount


        def change_relationship(self, relationship: str) -> None:
            if type(relationship) != str:
                raise rentale.RenTaleTypeError(str, type(relationship))
            
            self.relationship = relationship

        
        def change_note(self, note: str) -> None:
            if type(note) != str:
                raise rentale.RenTaleTypeError(str, type(note))

            self.note = note


# ============================== DYNAMIC MODIFICATION METHODS | PARTIAL ONLY ============================== #
        @property
        def color(self) -> str:
            val = self.who_args.get("color")
            return val if val is not None else gui.text_color

        @color.setter
        def color(self, value) -> None:
            self.who_args["color"] = value


        @property
        def what_color(self) -> str:
            val = self.what_args.get("color")
            return val if val is not None else gui.text_color

        @what_color.setter
        def what_color(self, value) -> None:
            self.what_args["color"] = value
