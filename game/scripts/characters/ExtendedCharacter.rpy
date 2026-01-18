init -11 python:
    from enum import Enum

    class StatType(Enum):
        Friendship = 0
        Love = 1
        Lust = 2


    class ExtendedCharacter(renpy.character.ADVCharacter):
        def __init__(self, name, color, relationship, **properties):
            # Init actual character
            super(ExtendedCharacter, self).__init__(name, color = color, **properties)
            # Base properties
            self.Name = str(name)
            self.Color = str(color)
            # Custom stats
            self.Friendship = int(0)
            self.Love = int(0)
            self.Lust = int(0)
            # Specific customisation
            self.Relationship = str(relationship)


        def IncreaseStat(self, stat: StatType, amount: int) -> None:
            if type(stat) != StatType:
                raise TypeError(f"Expected StatType, got {type(stat).__name__}")
            
            match stat:
                case StatType.Friendship:
                    self.Friendship += amount
                case StatType.Love:
                    self.Love += amount
                case StatType.Lust:
                    self.Lust += amount


        def DecreaseStat(self, stat: StatType, amount: int) -> None:
            if type(stat) != StatType:
                raise TypeError(f"Expected StatType, got {type(stat).__name__}")

            match stat:
                case StatType.Friendship:
                    self.Friendship -= amount
                case StatType.Love:
                    self.Love -= amount
                case StatType.Lust:
                    self.Lust -= amount


        def ChangeRelationship(self, relationShip: str) -> None:
            if type(relationShip) != str:
                raise TypeError(f"Expected string, got {type(relationShip).__name__}")
            
            self.Relationship = relationShip

