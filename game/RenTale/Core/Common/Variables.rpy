# =============== LOCATION SYSTEM =============== # 
define RenTale_ALL_LOCATIONS = dict() # Dictionary<Location, List<Event>>
default RenTale_CURRENT_LOCATION = None # Location

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
