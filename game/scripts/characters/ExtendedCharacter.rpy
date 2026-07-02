init -100 python:
    from enum import Enum

    class StatType(Enum):
        Friendship = 0
        Love = 1
        Lust = 2


init -100 python:
    class ExtendedCharacter(renpy.character.ADVCharacter):
        def __init__(self, name, color, note = "", relationship = "", **properties):
            if type(name) != str:
                raise RenTaleTypeError(str, type(name))
            if type(color) != str:
                raise RenTaleTypeError(str, type(color))
            if type(note) != str:
                raise RenTaleTypeError(str, type(note))
            if type(relationship) != str:
                raise RenTaleTypeError(str, type(relationship))
            # Init actual character
            super(ExtendedCharacter, self).__init__(name, color = color, **properties)
            # Base properties
            self.Name = name
            self.Color = color
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
                raise RenTaleTypeError(StatType, type(stat))
            if type(amount) != int:
                raise RenTaleTypeError(int, type(amount))
            
            match stat:
                case StatType.Friendship:
                    self.Friendship += amount
                case StatType.Love:
                    self.Love += amount
                case StatType.Lust:
                    self.Lust += amount


        def decrease_stat(self, stat: StatType, amount: int) -> None:
            if type(stat) != StatType:
                raise RenTaleTypeError(StatType, type(stat))
            if type(amount) != int:
                raise RenTaleTypeError(int, type(amount))

            match stat:
                case StatType.Friendship:
                    self.Friendship -= amount
                case StatType.Love:
                    self.Love -= amount
                case StatType.Lust:
                    self.Lust -= amount


        def change_relationship(self, relationship: str) -> None:
            if type(relationship) != str:
                raise RenTaleTypeError(str, type(relationship))
            
            self.Relationship = relationship
