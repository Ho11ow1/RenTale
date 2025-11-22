# RenTale
[![Status: Work In Progress](https://img.shields.io/badge/Status-Work%20In%20Progress-yellow.svg)](https://github.com/Ho11ow1/RenTale)
[![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-blue.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/license/MIT)<br/>
[![Ren'Py](https://img.shields.io/badge/Ren'Py-FF7F7F?logo=Renpy&logoColor=fff)](https://renpy.org)<br/>
**A type safe and utility full Ren'Py game template**<br/>
Designed to streamline Visual Novel development and avoid runtime errors

## Features
- **Object oriented design**
  - **Pure python classes** for better type safety and structure
  - **Enum based constants** for type safe state management
  - **Class methods** for organized, reusable functionality
  - **Singleton pattern support** through class level methods

- **Type safety**
  - **Runtime type validation** preventing invalid values at assignment
  - **Strong typing enforcment** on all custom elements
  - **Type checking on construction** on all elements
  - **Clear Error exceptions** names, error types, messages

- **Systems**
  - **ExtendedCharacter**: A wrapper around Ren'Py's Character class with built-in relationship tracking and stats
  - **FlagRef**: A strongly typed flag wrapper that ensures type safety at runtime

- **Managers**
  - **FlagManager**: Centralized flag management with type validation
  - **TimeManager**: Controls the day night cycle of the game
  - **SceneManager**: Wrapper for scene transitions with automatic UI cleanup

## Docs
- **[CharacterSystem](game/scripts/docs/CHARACTER_SYSTEM.md)**
- **[CreatingAreas](game/scripts/docs/CREATING_AREAS.md)**
- **[EventSystem](game/scripts/docs/GAME-EVENT_FLAGS.md)**

## Code Style

This template uses a **C# naming convention** rather than PEP 8:

- **Classes**: `PascalCase` (e.g., `ExtendedCharacter`, `FlagManager`)
- **Methods**: `PascalCase` (e.g., `Set()`, `Increment()`)
- **Public properties**: `PascalCase` (e.g., `Name`, `Friendship`)
- **Private members**: `_camelCase` (e.g., `_character`)
- **Files**: `PascalCase.rpy` matching class names

This choice prioritizes:
- Type safety and structure
- Consistency with statically-typed languages
- Clear visual distinction between elements

If you prefer traditional Python conventions (snake_case), feel free to adapt the template to your style.


## Requirements
- [Ren'Py SDK](https://renpy.org/latest.html) version 8.0 or higher
- Basic object oriented python knowledge (classes, methods, enums)
- Minimal Ren'Py scripting knowledge

## License

MIT License - see [LICENSE](LICENSE) 