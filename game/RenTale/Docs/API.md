# RenTale API Reference

> For user-level code including [`ExtendedCharacter`](UserAPI.md#extendedcharacter) and [`StatType`](UserAPI.md#stattype) see [UserAPI](UserAPI.md)

---

## [Actions](#actions)

### [MoveTo](#moveto)

```rpy
class MoveTo(Action):
    def __init__(self, location: Location)
```
- location: `Location`

> Navigates to the given location if it is unlocked. Internally calls [`RenTale_GoTo`](#rentale_goto).

### [SkipTime](#skiptime)

```rpy
class SkipTime(Action):
    def __init__(self, count: int = 1)
```
- count: `Int` - Number of time periods to advance. Defaults to `1`

> Advances the time of day `count` periods. 

> Automatically advances the day and week when necessary

---

## [Managers](#managers)

### [AudioManager](#audiomanager)

#### Static utility class for managing audio playback and volume across all channels.

```rpy
AudioManager.SetMasterVolume(volume: float) -> None
# Returns a value between 0.0 and 1.0
AudioManager.GetMasterVolume() -> float

AudioManager.PlayBGM(file: str, loop: bool = True, fadeIn: float = 0.0) -> None
AudioManager.StopBGM(fadeOut: float | None = 0.0) -> None
AudioManager.SetBGMVolume(volume: float) -> None
# Returns a value between 0.0 and 1.0
AudioManager.GetBGMVolume() -> float

AudioManager.PlaySFX(file: str, fadeIn: float = 0.0) -> None
AudioManager.StopSFX(fadeOut: float | None = 0.0) -> None
AudioManager.SetSFXVolume(volume: float) -> None
# Returns a value between 0.0 and 1.0
AudioManager.GetSFXVolume() -> float
AudioManager.PlayVO(file: str, fadeIn: float = 0.0) -> None
AudioManager.StopVO(fadeOut: float | None = 0.0) -> None
AudioManager.SetVOVolume(volume: float) -> None
# Returns a value between 0.0 and 1.0
AudioManager.GetVOVolume() -> float
```

| Channel | Description                         |
| ------- | ----------------------------------- |
| Master  | Affects all channels simultaneously |
| BGM     | Background music. Loops by default  |
| SFX     | Sound effects. Does not loop        |
| VO      | Voice over. Does not loop           |

> Volume values must be between `0.0` and `1.0`

### [TimeManager](#timemanager)

#### Static utility class for reading the current in-game time state.

```rpy
TimeManager.IsMorning() -> bool
TimeManager.IsNoon() -> bool
TimeManager.IsAfternoon() -> bool
TimeManager.IsEvening() -> bool
TimeManager.IsNight() -> bool
# Returns true if TimeOfDay < Evening
TimeManager.IsDaytime() -> bool
# Returns true if TimeOfDay >= Evening
TimeManager.IsNighttime() -> bool
# Returns true if Day != Saturday || Sunday
TimeManager.IsWeekday() -> bool
# Returns true if Day == Saturday || Sunday
TimeManager.IsWeekend() -> bool
TimeManager.GetTimeOfDayName() -> str
TimeManager.GetDayName() -> str
TimeManager.GetDayCount() -> int
TimeManager.GetWeek() -> int
```

> To advance time use the `SkipTime` action in a UI button or [`RenTale_Advance_Time(count: int = 1)`](#rentale_advance_time) directly.

---

## [Inventory](#inventory)

#### System class for managing items inside of the Inventory. Automatically populated when an [`InventoryItem`](#inventoryitem) instance is created

```rpy
Inventory.Add(item: InventoryItem) -> None
Inventory.Remove(item: InventoryItem) -> None
Inventory.Contains(item: InventoryItem) -> bool
```

---

## [Models](#models)

### [Event](#event)

```rpy
class Event():
    def __init__(self, name, location, isUnlocked = False, isAutomatic = False, isCompleted = False, unlockCondition = None, action = None)
```
| Parameter         | Type              | Default   | Description                                                                               |
|-------------------|-------------------|-----------|-------------------------------------------------------------------------------------------|
| name              | `String`          | required  | Unique name for the event                                                                 |
| location          | `Location`        | required  | Location this event belongs to                                                            |
| isUnlocked        | `Bool`            | `False`   | Whether the event is unlocked                                                             |
| isAutomatic       | `Bool`            | `False`   | Whether the event triggers automatically                                                  |
| isCompleted       | `Bool`            | `False`   | Whether the event has been completed                                                      |
| unlockCondition   | `String` or `None`| `None`    | Python expression evaluated to determine if event can unlock                              |
| action            | `String` or `None`| `None`    | Python expression(s) executed when the event plays. Separate multiple actions with `;`    |

#### Methods
```rpy
# Unlocks the event
Event.Unlock() -> None
# Returns True if unlockCondition is None or the UnlockCondition evaluates to True
Event.CheckCondition() -> bool
# Marks the Event as completed and executes action if not already completed
Event.Play() -> None
```

> `Event` must be created via `default` and their [`Location`](#location) must be initialized first.

> Use `init offset = 1` or higher in Event files to guarantee correct initialization order.

> The `UnlockCondition` and `Action` parameters go through an internal function which raises an error if the string contains forbidden actions for user safety.

> "Forbidden" actions are those which directly interact with the users system, This means things such as: import, os, sys, subprocess, exec, eval, open, etc... will be flagged.

### [FlagRef](#flagref)
#### Represents a simple type-safe wrapper for common / general game flags. Automatically registers into [`RenTale_All_Flags`](#rentale_all_flags) on creation.
```rpy
class FlagRef():
    def __init__(self, name, value)
```
- name: `String`
- value: `Int || Bool`

#### Methods
```rpy
# Sets the flag value. Raises an error if the value is different from the flags Value
FlagRef.Set(value: int | bool) -> None
# Toggles a Bool flag. Raises an error if the flag is an Int flag
FlagRef.Toggle() -> None
# Increments an Int flag. Raises an error if the flag is a Bool flag
FlagRef.Increment(amount: int = 1) -> None
# Decrements an Int flag. Raises an error if the flag is a bool flag
FlagRef.Decrement(amount: int = 1) -> None
```

> The `name` variable is used for event lookup / iteration using [`RenTale_All_Flags`](#rentale_all_flags)

> The type of `value` is locked on creation. Passing a different type to `Set()` will raise a [`RenTaleTypeError`](#rentaletypeerror).

> `FlagRef` must be created via `default`

> It is recommended to bundle multiple FlagRefs into a class created via `default` or create each FlagRef as a seperate `default`

### [GalleryItem](#galleryitem)
#### Represents a scene in the gallery. Automatically registers into [`RenTale_Gallery_List`](#rentale_gallery_list) and [`persistent.RenTale_Gallery`](#persistentrentale_gallery) on creation.
```rpy
class GalleryItem():
    def __init__(self, name, label, thumbnail, scope = None, isUnlocked = False)
```


| Parameter | Type                  | Default   | Description                           |
|-----------|-----------------------|-----------|---------------------------------------|
| name      | `String`              | required  | Unique name, used as persistent key   |
| label     | `String`              | required  | Ren'Py label to replay the scene      |
| thumbnail | `String`              | required  | Image path for the gallery grid       |
| scope     | `Dictionary` or `None`| `None`    | Scope passed to `Replay`              |
| isUnlocked| `Bool`                | `False`   | Default unlock state on first run     |

#### Methods
```rpy
# Unlocks the item in both the iterable list and persistent storage
GalleryItem.Unlock() -> None
```

> `GalleryItem` must be created via `define`

### [InventoryItem](#inventoryitem)
#### Represents an item in the player inventory. Automatically registers into `Inventory` on creation.
```rpy
class InventoryItem():
    def __init__(self, name, quantity, isStackable, image = None, description = "")
```

| Parameter     | Type              | Default   | Description                       |
|---------------|-------------------|-----------|-----------------------------------|
| name          | `String`          | required  | Unique name for the item          |
| quantity      | `Int`             | required  | Starting quantity                 |
| isStackable   | `Bool`            | required  | Whether quantity can be modified  |
| image         | `String` or `None`| `None`    | Image path for UI display         |
| description   | `String`          | `""`      | Item description                  |

#### Methods
```rpy
# Increases quantity if stackable
InventoryItem.Receive(quantity: int = 1) -> None
# Decreases quantity if stackable, floored at 0
InventoryItem.Remove(quantity: int = 1) -> None
```

> `InventoryItem` must be initialized via `default`

### [Location](#location)
#### Represents a navigable game location. Automatically registers into [`RenTale_All_Locations`](#rentale_all_locations) on creation.
```rpy
class Location():
    def __init__(self, name, label, isUnlocked = True)
```

| Parameter | Type      | Default   | Description                               |
|-----------|-----------|-----------|-------------------------------------------|
| name      | `String`  | required  | Unique name for the location              |
| label     | `String`  | required  | Ren'Py label to jump to on navigation     |
| isUnlocked| `Bool`    | `True`    | Whether the location can be navigated to  |

#### Methods
```rpy
# Unlocks the location
Location.Unlock() -> None
```

> `Location` must be initialized via `default` and before Events

---

## [Functions](#functions)

### [RenTale_GoTo](#rentale_goto)

```rpy
def RenTale_GoTo(location: Location) -> None
```
- location: `Location`

> Navigates to the given location if it exists and is unlocked. Sets `RenTale_Current_Location` and jumps to `location.Label`.

### [RenTale_TriggerAutomaticEvents](#rentale_triggerautomaticevents)

```rpy
def RenTale_TriggerAutomaticEvents() -> None
```

> Iterates all events at [`RenTale_Current_Location`](#rentale_current_location) and plays any that are unlocked, automatic, not completed and pass `CheckCondition()`.

> It is recommended to call this function at the top of each location label.

### [RenTale_Generate_Filtered_List](#rentale_generate_filtered_list)

```rpy
def RenTale_Generate_Filtered_List(prefix: str) -> set
```
- prefix: `String` — Name prefix to filter by

> Returns a filtered set of [`GalleryItem`](#galleryitem) objects from [`RenTale_Gallery_List`](#rentale_gallery_list) where `item.Name` starts with the given prefix. Used to populate `GalleryPage`.


### [RenTale_Advance_Time](#rentale_advance_time)

```rpy
def RenTale_Advance_Time(count: int = 1) -> None
```

> Advances the time of day `count` periods. 

> Automatically advances the day and week when necessary

---

## [Exceptions](#exceptions)

### [RenTaleTypeError](#rentaletypeerror)
#### Raised when an argument is of the wrong type.
```rpy
raise RenTaleTypeError(expected, got)
```
- expected: `type` or `tuple[type]` — The expected type(s)
- got: `type` — The received type via `type(value)`

### [RenTaleValueError](#rentalevalueerror)
#### Raised when an argument is the correct type but an invalid value.
```rpy
raise RenTaleValueError(expected, got)
```
- expected: `String` — Description of the expected value range
- got: value — The received value

### [RenTaleArgumentException](#rentaleargumentexception)
#### Raised when an operation is invalid for the current state regardless of argument type or value.
```rpy
raise RenTaleArgumentException(message)
```
- message: `String` — Description of why the operation is invalid

---

## [Variables](#variables)


### [RenTale_All_Characters](#rentale_all_characters)
#### Provides an iterable registry for all [`ExtendedCharacter`](UserAPI.md#extendedcharacter) instances.
```rpy
default RenTale_All_Characters = set() # HashSet<ExtendedCharacter>
```


### [RenTale_All_Flags](#rentale_all_flags)
#### Provides an iterable registry for all [`FlagRef`](#flagref) instances, allowing for data lookup, display, and modification.
```rpy
default RenTale_All_Flags = dict() # Dictionary<String, FlagRef>
```


### [RenTale_All_Locations](#rentale_all_locations)
#### Provides an iterable registry for all [`Locations`](#location) and their associated events.
```rpy
default RenTale_All_Locations = dict() # Dictionary<Location, List<Event>>
```

### [RenTale_Current_Location](#rentale_current_location)
#### Represents a reference to the current active [`Location`](#location).
```rpy
default RenTale_Current_Location = None # Location
```


### [RenTale_Gallery_List](#rentale_gallery_list)
#### Represents an iterable list of `GalleryItem` for the gallery.
```rpy
define RenTale_Gallery_List = set() # HashSet<GalleryItem> (Named list for simplicity, HashSet for uniqueness)
```


### [persistent.RenTale_Gallery](#persistent_rentale_gallery)
#### Represents a mapping that allows for game wide gallery unlocks.
```rpy
default persistent.RenTale_Gallery = dict() # Dictionary<Name, IsUnlocked> (Derived from GalleryItem)
```

> Although publicly accessible, this variable should not be touched or modified in any way, it purely exists as a reference to game wide data and nothing more.

> To unlock anything within the gallery please use [`GalleryItem.Unlock()`](#galleryitem)

---

## [Guidelines](#guidelines)

### Default vs Define
- Default variables will be stored under the store namespace which will increase save file size
- Define variables will be re-created at startup time and never stored

- - `Default` | Location, Event, InventoryItem, FlagRef (state must persist across saves)
- - `Define` | GalleryItem (unlock state lives in persistent, object reconstructed on startup)

### DocStrings
#### All methods for each class have simple docstrings to explain what each methods does, renpy support for intellisense isn't the best and as such they are less detailed than this Document

If you find any issues during usage, please create a github Issue [Here](https://github.com/Ho11ow1/RenTale/issues)
