# RenTale UserAPI Reference

> User-level code lives under `game/scripts/` and is provided as `.rpy` files for full modification.

> For core RenTale systems see [API](API.md)

---

## [StatType](#stattype)

```rpy
class StatType(Enum):
    Friendship = 0
    Love = 1
    Lust = 2
```

> `StatType` is user-modifiable. Add or remove stats to fit your game's needs.

---

## [ExtendedCharacter](#extendedcharacter)
#### Extends Ren'Py's `ADVCharacter` with relationship stats and a modifiable relationship label.
```rpy
class ExtendedCharacter(ADVCharacter):
    def __init__(self, name, color, relationship = "", **properties)
```

| Parameter    | Type     | Default | Description                               |
|--------------|----------|---------|-------------------------------------------|
| name         | `String` | required| Character display name                    |
| color        | `String` | required| Dialogue name color                       |
| relationship | `String` | `""`    | Relationship label shown in UI            |
| **properties |          |         | Any additional Ren'Py character properties|

#### Stats
| Stat       | Type  | Default | Description          |
|------------|-------|---------|----------------------|
| Friendship | `Int` | `0`     | Can be negative      |
| Love       | `Int` | `0`     | Can be negative      |
| Lust       | `Int` | `0`     | Can be negative      |

#### Methods
```rpy
# Increases the given stat by amount
ExtendedCharacter.IncreaseStat(stat: StatType, amount: int) -> None
# Decreases the given stat by amount. Stats can go negative
ExtendedCharacter.DecreaseStat(stat: StatType, amount: int) -> None
# Changes the relationship label
ExtendedCharacter.ChangeRelationship(relationship: str) -> None
```

#### Example
```rpy
default Willow = ExtendedCharacter("Willow", color = "#1b1b1b", relationship = "The weeping one")

# Increase friendship via event action
action = "Willow.IncreaseStat(StatType.Friendship, 10); renpy.call('event_willow_meeting')"

# Conditional stat change inside a label
label event_willow_meeting:
    menu:
        "Be kind":
            $ Willow.IncreaseStat(StatType.Love, 5)
        "Be rude":
            $ Willow.DecreaseStat(StatType.Friendship, 10)

    return
```

> `ExtendedCharacter` works alongside standard Ren'Py `Character` instances.

>Use `Character` for narrators and minor characters, `ExtendedCharacter` for love interests and important NPCs.

> `ExtendedCharacter` must be initialized via `default` just like standard `Character`

---

If you find any issues during usage, please create a github Issue [Here](https://github.com/Ho11ow1/RenTale/issues)
