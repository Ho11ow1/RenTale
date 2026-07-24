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
    friendship = 0
    love = 1
    lust = 2
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
    def color(self) -> str:
@Color.setter
    def color(self, value) -> None:

@property
    def what_color(self) -> str:
@WhatColor.setter
    def what_color(self, value) -> None:
```
#### Example usage:
```rpy

# After this statement when Alexandra says anything or anyone says [Alexandra.name] it will show as "Alex"
$ Alexandra.name = "Alex"

# With this scope when Isabella speaks in the replay her name will be "Bella" and her dialogue color will be pink
scope = {
    "Isabella.name": "Bella",
    "Isabella.what_color": "#F9A8B4"
}
```
| Property/Setter           | Return Type              | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| name | `str`/`None` | Allows for character name modification and retrieval       |
| color | `str`/`None` | Allows for character name color modification and retrieval |
| what_color | `str`/`None` | Allows for character text color modification and retrieval |

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
