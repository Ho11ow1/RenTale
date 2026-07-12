# RenTale API Documentation
## Everything in this document can be found under the `rentale` namespace.

> For user-level code such as `ExtendedCharacter` or `Discord RPC` see [UserAPI](UserAPI.md)

---

## Quick navigation
| Type                      | Description              |
| :------------------------ | :----------------------- |
| [Action](#actions)        | RenTale Actions          |
| [Variable](#variables)    | RenTale Variables        |
| [Function](#functions)    | RenTale Functions        |
| [Exception](#exceptions)  | Rentale Exceptions       |
| [Model](#models)          | Rentale system models    |
| [Manager](#managers)      | Rentale manager classes  |
| [Guidelines](#guidelines) | Rentale usage guidelines |

---

# [Action](#actions)

## [FilePageJump](#actions_filepagejump)
> This action mimics the default behaviour of the `FilePageNext()` and `FilePagePrevious()` built-in actions but with the added ability of specifying the step count.
```py
class FilePageJump(renpy.store.Action):
    def __init__(self, max: int | None = None, wrap: bool = False, auto: bool = True, quick: bool = True, step: int = 1)
```
| Parameter                  | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| max                       | `int` or `None`              | If not None, sets the max file page allowed to move to  |
| wrap                       | `bool`              | if True and max if not None, allows wrapping from max to 1 and from 1 to max  |
| auto                       | `bool`              | if True and config.has_autosave, allows stepping onto the auto save page  |
| quick                       | `bool`              | if True and config.has_quicksave, allows stepping onto the quick save page  |


## [MoveTo](#actions_moveto)
> This action is used in tandem with the [`Location`](#models_location) Model and uses [`go_to`](#functions_go_to) internally to jump to the specified locations label if it is unlocked
```py
class MoveTo(renpy.store.Action):
    def __init__(self, location: Location)
```
| Parameter                  | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| location | [`Location`](#models_location) | Specifies the location to use for the action|


## [SkipTime](#actions_skiptime)
> This action is used to advance time related variables which can be found under [`Variables.Time`](#variables_time)
```py
class SkipTime(renpy.store.Action):
    def __init__(self, count: int = 1)
```
| Parameter                  | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| count | `int` | Specifies the amount of times of day to move forward - Automatically advances the day and week if necessary|

---

# [Variable](#variables)

## [Developer](#variables_developer)
> These specific variables exist to helper developers debug what's currently happening with specific ties to RenTale
```rpy
default all_characters = set()
default all_flags = dict()
default all_locations = dict()
```
| Variable                  | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| all_characters | set<[`ExtendedCharacter`](UserAPI.md#models_extendedcharacter)>| Allows viewing of all [`ExtendedCharacter`](UserAPI.md#models_extendedcharacter) instances - Auto-populated  |
| all_flags | dict<`str`, [`FlagRef`](#models_flagref)>| Allows viewing of all [`FlagRef`](#models_flagref) instances and their associated names - Auto-populated  |
| all_locations | dict<[`Location`](#models_location), List<[`Event`](#models_event)>>| Allows viewing of all [`Location`](#models_location) and a list of their associated [`Event`](#models_event) - Auto-populated  |
| current_location | [`Location`](#models_location)| Specifies the current location the player is in - Set via the [`go_to`](#functions_go_to) or the [`MoveTo`](#actions_moveto) Action  |


## [Time](#variables_time)
> These specific variables exist to implement a week based time system for your game
```rpy
define time_of_day_names = [ "Morning", "Noon", "Afternoon", "Evening", "Night"]
define day_names = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
define weekend_indexes = [ 5, 6 ]

default time_of_day_num = 0
default day_count = 1
default day_name = rentale.day_names[0]
default week = 1
```
| Variable                  | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| time_of_day_names  |  list<`str`> | Defines the times of day your game will use |
| day_names  | list<`str`>  | Defines the days and and order which your game will use |
| weekend_indexes  | list<`str`>  | Defines the indexes that will constitute a "weekend" day. This is a variable as different games want to order their days differently |
| time_of_day_num  | `int`  | Holds the index of the time of day so we can easily advance through the time system |
| day_count  | `int`  | Holds the number of days that have passed |
| day_name  |  `str` | Holds the name of the current day |
| week  |  `int` | Holds the numer of weeks that have passed |


## [Gallery](#variables_gallery)
> These specific variables exist to implement an easy to use gallery system for your game
```rpy
default persistent.rentale_gallery = dict()
define gallery_list = set()
```
| Variable                  | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| persistent.rentale_gallery  |  dict<`str`, `bool`> | Holds the persistent state of each [`GalleryItem`](#models_galleryitem) as a name, isUnlocked kvp - Should not be touched manually  |
| gallery_list  | set<[`GalleryItem`](#models_galleryitem)>  |  Holds [`GalleryItem`](#models_galleryitem) references so that they can be used and displayed in a gallery screen - Auto-populated |


## [Inventory](#variables_inventory)
> These specific variables exist to implement an easy to use inventory system for your game
```rpy
default inventory = rentale.Inventory()
```
| Variable                  | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| inventory | [`Inventory`](#managers_inventory) | An instance of the [`Inventory`](#managers_inventory) manager class to provide save based inventory management |

---

# [Function](#functions)

## [go_to](#functions_go_to)
> Navigates to the given location if it exists and is unlocked
```py
def go_to(location: Location) -> None
```
| Parameter                  | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| location | [`Location`](#models_location) | Specifies the [`location`](#models_location) to move to |


## [trigger_automatic_events](#functions_trigger_automatic_events)
> Triggers all automatic events at the current location that are unlocked, pass their condition and have not been completed
```py
def trigger_automatic_events() -> None
```


## [generate_filtered_list](#functions_generate_filtered_list)
> Returns a filtered set of [`GalleryItem`](#models_galleryitem) where the item name starts with the given prefix
```py
def generate_filtered_list(prefix: str) -> set
```
| Parameter                  | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| prefix | `str` | Specifies the string used to filter the gallery list, Only items whos names begins with `prefix` will be returned in the set |


## [advance_time](#functions_advance_time)
> Advances the time of day by the specified amount of times
```py
def advance_time(count: int = 1) -> None
```
| Parameter                  | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| count | `int` | Specifies the amount of times to advance the time of day - Automatically advances day and week when necessary |


## [advance_days](#functions_advance_days)
> Advances the specified amount of days within the week
```py
def advance_days(count: int = 1) -> None
```
| Parameter                  | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| count | `int` | Specifies the amount of days to advance by - Automatically advances week when necessary |


## [advance_weeks](#functions_advance_weeks)
> Advances the specified amount of weeks 
```py
def advance_weeks(count: int = 1) -> None
```
| Parameter                  | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| count | `int` | Specifies the amount of weeks to advance by |


---

# [Exception](#exceptions)

## [RenTaleArgumentException](#exceptions_rentaleargumentexception)
> This exception is raised when a parameter type is correct and the value is correct but something is just not allowed or went wrong | Example: "Cannot increment a 'Bool' flag"
```py
class RenTaleArgumentException(Exception)
```

## [RenTaleTypeError](#exceptions_rentaletypeerror)
> This exception is raised when a parameter type is incorrect | Example: "Expected 'int' got 'str'"
```py
class RenTaleTypeError(TypeError)
```

## [RenTaleValueError](#exceptions_rentalevalueerror)
> This exception is raised when a parameter is outside of the allowed range | Example: "Expected: positive number, got: -1"
```py
class RenTaleValueError(ValueError)
```

---

# [Model](#models)

## [Event](#models_event)
> Creates an Event object which is associated with a Location allowing for automatic or manual event execution - Gets automatically added to: [`all_locations`](#variables_developer)
```py
class Event():
    def __init__(self, name, location, label, isUnlocked = False, isAutomatic = False, isCompleted = False, unlockCondition = None)
```
| Parameter                 | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| name | `str` | A unique name for this event |
| location | [`Location`](#models_location) | A location to which this event is connected to |
| label | `str` | A renpy label that will be called when this event is played |
| isUnlocked | `bool` | Defines if this event is already unlocked for the player |
| isAutomatic | `bool` | Defines if this event will be played via the [`trigger_automatic_event`](#functions_trigger_automatic_events) functioon |
| isCompleted | `bool` | States whether this event has already been played or not |
| unlockConditioon | `str` or `None` | If not none defines the condition that must evaluate to true so that the event can play. If none no check is made |

### Methods
```py
def unlock(self) -> None:
def check_condition(self) -> bool:
def play(self) -> None:
```
| Method                    | Return Type              | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| unlock | `None` | Unlocks this event if it has not already been unlocked |
| check_condition | `bool` | Returns true if the `unlockCondition` is None or evaluates to True |
| play | `None` | Calls the associated renpy label if this event has not been completed and `check_condition` returns True |


## [FlagRef](#models_flagref)
> Acts as a small wrapper around basic flags providing type-safety for future usage - Gets automatically added to: [`all_flags`](#variables_developer)
```py
class FlagRef():
    def __init__(self, name, value)
```
| Parameter                 | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| name | `str` | A unique name for this flag |
| value | `int` or `bool` | Defines the type of this flag - Locked at creation |

### Methods
```py
def set(self, value: int | bool) -> None:
def toggle(self) -> None:
def increment(self, amount: int = 1) -> None:
def decrement(self, amount: int = 1) -> None:
```
| Method                    | Return Type              | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| set | `None` | Sets this flags value to `value` |
| toggle | `None` | Toggles this flags value if it is a `bool` - True to False and vice-versa |
| increment | `None` | Increments this flags value by `amount` if this flags `value` type is an `int` |
| decrement | `None` | Decrements this flags value by `amount` if this flags `value` type is an `int` |


## [GalleryItem](#models_galleryitem)
> Creates an object which can then be displayed in a gallery screen - Always define this variable - Gets automatically added to: [`persistent.rentale_gallery`](#variables_gallery) and [`gallery_list`](#variables_gallery)
```py
class GalleryItem():
    def __init__(self, name, label, thumbnail, scope = None, isUnlocked = False)
```
| Parameter                 | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| name | `str` | A unique name for this item |
| label | `str` | A renpy label which will be called on executing the renpy `Replay()` Action |
| thumbnail | `str` | A filepath for the image to be shown on the gallery screen |
| scope | `dict` or `None` | A dictionary mapping variable name to value. These variables are set when entering the replay |
| isUnlocked | `bool` | Dictates whether this item is unlocked or not |

### Methods
```py
def unlock(self) -> None:
```
| Method                    | Return Type              | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| unlock | `None` | Unlocks this item if it is not already unlocked |


## [InventoryItem](#models_inventoryitem)
> Creates an object which can be used in the [`Inventory`](#managers_inventory) - Gets automatically added to the [`Inventory`](#managers_inventory)
```py
class InventoryItem():
    def __init__(self, name, quantity, isStackable, image = None, description = "")
```
| Parameter                 | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| name | `str` | A unique name for this item |
| quantity | `int` | Defines the initial quantity of this item in the inventory |
| isStackable | `bool` | Defines if this item can be received / removed (stacked) |
| image | `str` or `None` | A filepath for the image to be shown on the inventory screen |
| description | `str` | A description for this item which can be show in the inventory screen |

### Methods
```py
def receive(self, quantity: int = 1) -> None:
def remove(self, quantity: int = 1) -> None:
```
| Method                    | Return Type              | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| receive | `None` | Increases the quantity of this item by `quantity` if it is stackable |
| remove | `None` | Decreases the quantity ofthis item by `quantity` if it is stackable - limited to 0 |


## [Location](#models_location)
> Represents a navigable game location - Gets automatically added to: [`all_locations`](#variables_developer)
```py
class Location():
    def __init__(self, name, label, isUnlocked = True)
```
| Parameter                 | Type                     | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| name | `str` | A unique name for this location |
| label | `str` | A renpy label to which this object is tied to |
| isUnlocked | `bool` | Dictates whether this location is unlocked and available or not |

### Methods
```py
def unlock(self) -> None
```
| Method                    | Return Type              | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| unlock | `None` | Unlocks this location if it is not already unlocked |

---

# [Manager](#managers)

## [Inventory](#managers_inventory)
> Represents a save based inventory system which is easily accessed via: [`inventory`](#variables_inventory)
```py
class Inventory():
    def __init__(self):
        self.Items = set()
```

### Methods
```py
def add(self, item: InventoryItem) -> None:
def remove(self, item: InventoryItem) -> None:
def contains(self, item: InventoryItem) -> bool:
```
| Method                    | Return Type              | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| add | `None` | Adds the specified [`InventoryItem`](#models_inventoryitem) to the inventory if it is not already in the inventory |
| remove | `None` | Removes the specified [`InventoryItem`](#models_inventoryitem) from the inventory if it is found in the inventory |
| contains | `bool` | Returns true if the specified [`InventoryItem`](#models_inventoryitem) is found in the inventory |


## [TimeManager](#managers_timemanager)
> Allows for getting state data for all [`Time Variables`](#variables_time)
```py
class TimeManager()
```

### Methods
```py
def is_morning() -> bool:
def is_noon() -> bool:
def is_afternoon() -> bool:
def is_evening() -> bool:
def is_night() -> bool:

def is_daytime() -> bool:
def is_nighttime() -> bool:
def is_weekday() -> bool:
def is_weekend() -> bool:

def get_day_count() -> int:
def get_week() -> int:
def get_day_name() -> str:
def get_time_of_day_name() -> str:
```
| Method                    | Return Type              | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| is_morning | `bool` | Returns True if the current time of day is "Morning"|
| is_noon | `bool` | Returns True if the current time of day is "Noon"|
| is_afternoon | `bool` | Returns True if the current time of day is "Afternoon"|
| is_evening | `bool` | Returns True if the current time of day is "Evening"|
| is_night | `bool` | Returns True if the current time of day is "Night"|
| | | |
| is_daytime | `bool` | Returns true if the current time of day is earlier than "Evening" |
| is_nighttime | `bool` | Returns true if the current time of day is later than "Afternoon" |
| is_weekday | `bool` | Returns true if the current day is a week day |
| is_weekend | `bool` | Returns true if the current day is not a week day |
| | | |
| get_day_count | `int` | Returns the amount of days that have passed since starting the save |
| get_week | `int` | Returns the amount of weeks that have passed since starting the save |
| get_day_name | `str` | Returns the name of the current day in the time system |
| get_time_of_day_name | `str` | Returns the name of the current time of day in the time system |


## [AudioManager](#managers_audiomanager)
> Serves as an alternative way to play audio and modify values on built-in and custom channel - Does not use renpy.voice
```py
class TimeManager()
```

### Methods
```py
def play_music(file: str, loop: bool = True, fadeIn: float = 0.0, fadeOut: float | None = None, tight: bool = False, ifChanged: bool = False) -> None:
def stop_music(fadeOut: float | None = None) -> None:
def set_music_volume(cls, volume: float) -> None:
def get_music_volume(cls) -> float:

def play_sound(file: str, fadeIn: float = 0.0, ifChanged: bool = False) -> None:
def stop_sound(fadeOut: float | None = None) -> None:
def set_sound_volume(cls, volume: float) -> None:
def get_sound_volume(cls) -> float:

def play_voice(file: str, fadeIn: float = 0.0, ifChanged: bool = False) -> None:
def stop_voice(fadeOut: float | None = None) -> None:
def set_voice_volume(cls, volume: float) -> None:
def get_voice_volume(cls) -> float:

def play_custom(file: str, channel: str, loop: bool = False, fadeIn: float = 0.0, fadeOut: float | None = None, tight: bool = False, ifChanged: bool = False) -> None:
def stop_custom(channel: str, fadeOut: float | None = None) -> None:
def set_custom_volume(channel: str, volume: float) -> None:
def get_custom_volume(channel: str) -> float:
```
| Method                    | Return Type              | Description                                             |
| :------------------------ | :----------------------- | :------------------------------------------------------ |
| play_music | `None` | Plays the specified `audio file` on the `music` channel|
| stop_music | `None` | Stops whatever is currently playing on the `music` channel|
| set_music_volume | `None` | Sets the volume of the `music` channel|
| get_music_volume | `float` | Returns the current volume of the `music` channel|
| | | |
| play_sound | `None` | Plays the specified `audio file` on the `sound` channel|
| stop_sound | `None` | Stops whatever is currently playing on the `sound` channel|
| set_sound_volume | `None` | Sets the volume of the `sound` channel|
| get_sound_volume | `float` | Returns the current volume of the `sound` channel|
| | | |
| play_voice | `None` | Plays the specified `audio file` on the `voice` channel|
| stop_voice | `None` | Stops whatever is currently playing on the `voice` channel|
| set_voice_volume | `None` | Sets the volume of the `voice` channel|
| get_voice_volume | `float` | Returns the current volume of the `voice` channel|
| | | |
| play_custom | `None` | Plays the specified `audio file` on the specified `channel`|
| stop_custom | `None` | Stops whatever is currently playing on the specified `channel`|
| set_custom_volume | `None` | Sets the volume of the specified `channel`|
| get_custom_volume | `float` | Returns the current volume of the specified `channel`|
> voice methods play audio on the voice channel rather than using renpy.voice as running it may break renpy auto-voicing and thus id-generation

---

# [Guidelines](#guidelines)
- [Locations](#models_location) must be created before any [Events](#models_event)
- [GalleryItem](#model_galleryitem)'s should be defined rather than defaulted

