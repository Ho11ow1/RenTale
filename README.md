# RenTale
[![Version: 2.0.0](https://img.shields.io/badge/Version-2.0.0-blue.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/license/MIT)<br/>
**A strongly typed Ren'Py framework for building Visual Novels without the usual runtime chaos.**<br/>
Locations, Events, Characters, Inventory, Audio, Time, Gallery, and Flags all ready to go.

---
## Features

### Systems
- `Location`, `Event`, `FlagRef`, `Inventory`, and `Gallery` systems, all type-checked and auto-registered.

### Characters
- `ExtendedCharacter` wraps Ren'Py's built-in character with relationship stats and labels.

### Managers
- Static utility classes for Audio and Time

### Type Safety
- Runtime validation, custom exceptions, and sandboxed event actions.

### Build
- Custom pipeline that strips junk and packages assets into deterministic RPA archives.
- Each concern gets its own archive — RenTale core, user scripts, audio, and other assets are all separated.

---
## Quick Example
```rpy
# Define locations
default L_City = Location("City", "label_city")
default L_Park = Location("Park", "label_park", isUnlocked = False)
 
# Define a character
default Willow = ExtendedCharacter("Willow", color = "#1b1b1b", relationship = "The weeping one")
 
# Define an event
default E_Meet_Willow = Event(
    name = "Meet_Willow",
    location = L_City,
    isUnlocked = True,
    isAutomatic = True,
    action = (
        "AudioManager.PlaySFX('audio/SFX/EventNotification.mp3');"
        "Willow.IncreaseStat(StatType.Friendship, 10);"
        "L_Park.Unlock();" 
        "renpy.call('Label_Event_Meet_Willow');"
    )
)

# In a location label
label label_city:
    $ RenTale_TriggerAutomaticEvents()
    # ...
```

---

## Docs
| Reference                 | Description                                                                   |
|---------------------------|-------------------------------------------------------------------------------|
| [API.md](game/RenTale/Docs/API.md)          | Core framework — all models, managers, functions, variables, and exceptions   |
| [UserAPI.md](game/RenTale/Docs/UserAPI.md)  | User-level code — `ExtendedCharacter`, `StatType`, modification guide         |

---
 
## Code Style
RenTale uses a **C# naming convention** rather than PEP 8:
 
| Element           | Convention          | Example                           |
|-------------------|---------------------|-----------------------------------|
| Classes           | `PascalCase`        | `ExtendedCharacter`, `FlagRef`    |
| Methods           | `PascalCase`        | `Set()`, `Increment()`, `Unlock()`|
| Public functions  | `RenTale_PascalCase`| `RenTale_TriggerAutomaticEvents()`|
| Private functions | `RenTale_snake_case`| No example as they're internal    |
| Public properties | `PascalCase`        | `Name`, `Friendship`              |
| Files             | `PascalCase.rpy`    | matches class name                |
 
> This prioritises consistency with statically-typed languages and keeps RenTale internals visually distinct from user code.

> If you prefer `snake_case`, nothing stops you from adapting things to your own style.

---
## Requirements
- [Ren'Py SDK](https://renpy.org/latest.html) version 8.0 or higher
- Basic Python OOP knowledge (classes, methods, enums)
- Minimal Ren'Py scripting knowledge

---
## License
MIT License - see [LICENSE](LICENSE)

If you find any issues during usage, please create a github Issue [Here](https://github.com/Ho11ow1/RenTale/issues)
