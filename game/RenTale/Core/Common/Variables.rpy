init offset = -999

# =============== LOCATION SYSTEM =============== # 
define RenTale_All_Locations = dict() # Dictionary<Location, List<Event>>
default RenTale_Current_Location = None # Location

# =============== TIME SYSTEM =============== #
define RenTale_time_of_day_names = [ "Morning", "Noon", "Afternoon", "Evening", "Night"]
define RenTale_day_names = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
define RenTale_days_per_week = 7
define RenTale_weekend_indexes = [ 5, 6 ]

default RenTale_time_of_day_num = 0
default RenTale_time_of_day_name = RenTale_time_of_day_names[0]
default RenTale_day_count = 1
default RenTale_day_name = RenTale_day_names[0]
default RenTale_week = 1

# =============== GALLERY SYSTEM =============== #
default persistent.RenTale_Gallery = dict() # Dictionary<Name, IsUnlocked> (Derived from GalleryItem)
define RenTale_Gallery_List = set() # HashSet<GalleryItem> (Named list for simplicity, HashSet for uniqueness)

# =============== INVENTORY SYSTEM =============== #
default Inventory = RenTale_Inventory()
