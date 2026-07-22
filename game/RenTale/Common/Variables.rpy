init offset = -999

# =============== CHARACTERS =============== #
default rentale.all_characters = set() # HashSet<ExtendedCharacter>

# =============== FLAGREFS =============== #
default rentale.all_flags = dict() # Dictionary<String, FlagRef>

# =============== LOCATION SYSTEM =============== # 
default rentale.all_locations = dict() # Dictionary<Location, List<Event>>
default rentale.current_location = None # Location

# =============== TIME SYSTEM =============== #
define rentale.time_of_day_names = [ "Morning", "Noon", "Afternoon", "Evening", "Night"]
define rentale.day_names = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
define rentale.weekend_indexes = [ 5, 6 ]

default rentale.time_of_day_num = 0
default rentale.day_count = 1
default rentale.day_name = rentale.day_names[0]
default rentale.week = 1

# =============== GALLERY SYSTEM =============== #
default persistent.rentale_gallery = dict() # Dictionary<Name, IsUnlocked> (Derived from GalleryItem)
define rentale.gallery_list = set() # HashSet<GalleryItem> (Named list for simplicity, HashSet for uniqueness)

# =============== INVENTORY SYSTEM =============== #
default rentale.inventory = rentale.Inventory()
default rentale.all_items = set()

# =============== SAFETY =============== #
init python in rentale:
    import re

    _blacklisted_patterns = [
        r'\bos\b',
        r'\bsys\b',
        r'\bimport\b',
        r'\b__import__\b',
        r'\bsubprocess\b',
        r'\bopen\b',
        r'\beval\b',
        r'\bexec\b',
        r'\bcompile\b',
        r'\b__builtins__\b',
        r'\bgetattr\b',
        r'\bsetattr\b',
    ]
    _blacklisted_regex = re.compile('|'.join(_blacklisted_patterns), re.IGNORECASE)
