# RenTale
[![Version: 2.1.0](https://img.shields.io/badge/Version-2.1.0-blue.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/license/MIT)<br/>
**A strongly typed Ren'Py framework for building Visual Novels without the usual runtime chaos.**<br/>
Events, Flags, Gallery, Locations and more ready out of the box.

---
## Features

### Systems
- `Event`, `FlagRef`, `Gallery`, `Inventory`, and `Location`, type-checked and auto-registered on creation.

### Managers
- Static utility classes for `Audio` and `Time`, with a consistent get/set-style API

### Type Safety
- Runtime type validation with custom Exceptions and sandboxed event actions

### Build
- Custom pipeline that strips junk and packages assets into deterministic RPA archives.
- Each concern gets its own archive — RenTale core, user scripts, images, and other assets are all separated.

---
## Quick Example
```rpy
# Define locations
default L_City_Library = rentale.Location("Library", "Label_City_Library", isUnlocked = False)
default L_City_Park = rentale.Location("Park", "Label_City_Park", isUnlocked = False)
 
# Define a character
default Alice = ExtendedCharacter("Alice", color = "#fbe7a1", note = "Creepy woman", relationship = "Stranger", what_color = "#fbe7a1")
 
# Define an event
default E_Meet_Alice = rentale.Event(
    name = "Meet_Alice",
    location = L_City_Park,
    label = "Label_Event_Park_1",
    unlockCondition = "E_Meet_Willow.IsCompleted"
)

# In a location label
label Label_City_Main:

    $ rentale.trigger_automatic_events()
    # ...
```

---

## Docs
| Reference                 | Description                                                                   |
|---------------------------|-------------------------------------------------------------------------------|
| [API.md](game/RenTale/Docs/API.md)          | Core framework — all models, managers, functions, variables, and exceptions   |
| [UserAPI.md](game/RenTale/Docs/UserAPI.md)  | User-level code — `ExtendedCharacter`, `StatType`, modification guide         |

---
## Requirements
- [Ren'Py SDK](https://renpy.org/latest.html) version 8.0 or higher
- Basic Python OOP knowledge (classes, methods, enums)
- Minimal Ren'Py scripting knowledge

### Additional
- To allow for Discord Rich Presence follow the Ren'Py docs [Here](https://www.renpy.org/doc/html/python.html#first-and-third-party-python-modules-and-packages)
- Or simply navigate to your project directory and paste this into the command line:
```bash
pip install --target game/python-packages pypresence
```

---

## Credits
- This template takes inspiration from multiple games by multiple developers
- As a source of providing credit to those that have insipired me please checkout [CREDITS](CREDITS.txt)

---

## License
MIT License - see [LICENSE](LICENSE)

If you find any issues during usage, please create a github Issue [Here](https://github.com/Ho11ow1/RenTale/issues)
