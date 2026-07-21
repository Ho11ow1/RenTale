init offset = 1

default E_City_Unlock_All = rentale.Event(
    name = "Unlock_City",
    location = L_City_Main,
    label = "Label_Event_City_1",
    is_unlocked = True,
    is_automatic = True
)

default E_Meet_Willow = rentale.Event(
    name = "Meet_Willow",
    location = L_City_Library,
    label = "Label_Event_Library_1",
    is_unlocked = True
)

default E_Meet_Alice = rentale.Event(
    name = "Meet_Alice",
    location = L_City_Park,
    label = "Label_Event_Park_1",
    unlock_condition = "E_Meet_Willow.is_completed"
)
