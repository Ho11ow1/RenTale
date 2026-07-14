# RenTale User-level API Documentation
## Everything in this document can be found under the default `renpy` namespace. No prefixing with `rentale.` is required

---

## Quick navigation
| Type                       | Description                      |
| :------------------------- | :------------------------------- |
| [Model](#models)           | User level models                |
| [Integration](#integration)| User level platfrom integrations |

---

# [Model](#models)

## [StatType](#models_stattype)
> A simple enum defining the trackable stat categories for an [`ExtendedCharacter`](#models_extendedcharacter)
```py
class StatType(Enum):
    Friendship = 0
    Love = 1
    Lust = 2
```


## [ExtendedCharacter](#models_extendedcharacter)
> Extends Ren'Py's ADVCharacter with relationship stats, a bio note, and a relationship label - Gets automatically added to: [`all_characters`](API.md#variables_developer)
```py
class ExtendedCharacter(renpy.character.ADVCharacter):
    def __init__(self, name, note = "", relationship = "", **properties):
```
| Parameter                 | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| name | `str` | The character's display name |
| note | `str` | A short bio note - Example: for a character card note |
| relationship | `str` | This character's relation to the player |
| **properties | `**kwargs` | Any additional properties passed through to the Ren'Py `Character()` class Example: `color = "#F9A4C7", what_color = "#d7d1a9"`

### Methods
```py
def increase_stat(self, stat: StatType, amount: int) -> None:
def decrease_stat(self, stat: StatType, amount: int) -> None:
def change_relationship(self, relationship: str) -> None:
def change_note(self, note: str) -> None:
```
| Method                    | Return Type              | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| increase_stat | `None` | Increases the given `stat` by `amount` |
| decrease_stat | `None` | Decreases the given `stat` by `amount` |
| change_relationship | `None` | Sets this characters `Relationship` to `relationship` |
| change_note | `None` | Sets this characters `Note` to `note` |

### Extras
> Intellisense for these properties varies
```py
@property
    def Name(self) -> str:
@Name.setter
    def Name(self, value) -> None:

@property
    def Color(self) -> str:
@Color.setter
    def Color(self, value) -> None:

@property
    def WhatColor(self) -> str:
@WhatColor.setter
    def WhatColor(self, value) -> None:
```
#### Example usage:
```rpy

# After this statement when Alexandra says anything or anyone says [Alexandra.Name] it will show as "Alex"
$ Alexandra.Name = "Alex"

# With this scope when Isabella speaks in the replay her name will be "Bella" and her dialogue color will be pink
scope = {
    "Isabella.Name": "A",
    "Isabella.WhatColor": "#F9A8B4"
}
```
| Property/Setter           | Return Type              | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| Name | `str`/`None` | Allows for character name modification in game and in gallery replay scope       |
| Color | `str`/`None` | Allows for character name color modification in game and in gallery replay scope |
| WhatColor | `str`/`None` | Allows for character text color modification in game and in gallery replay scope |

---

# [Integration](#integrations)

## [Discord](#integrations_discord)
> A wrapper around `pypresence` for managing Discord Rich Presence status
```py
class Discord():
    state_dict = {}
```

### Methods
```py
def init(cls) -> None:
def update(cls, dictKey: str) -> None:
```
| Method                    | Return Type              | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| init | `None` | Connects with the currently running discord client |
| update | `None` | Updates the rich presence with information at the given key from `state_dict`|
