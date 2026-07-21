init offset = 1

default E_Bedroom_Event_1 = rentale.Event(
    name = "Home_Bedroom_Intro",
    location = L_Home_Bedroom,
    label = "Label_Event_Bedroom_1",
    is_unlocked = True,
    is_automatic = True
)

default E_Kitchen_Event_1 = rentale.Event(
    name = "Home_Kitchen_1",
    location = L_Home_Kitchen,
    label = "Label_Event_Kitchen_1",
    is_automatic = True, 
    unlock_condition = "E_Bedroom_Event_1.is_completed"
)

default E_Bathroom_Event_1 = rentale.Event(
    name = "Home_Bathroom_1",
    location = L_Home_Bathroom,
    label = "Label_Event_Bathroom_1",
    is_automatic = True,
    unlock_condition = "E_Kitchen_Event_1.is_completed"
)

default E_Garden_Event_1 = rentale.Event(
    name = "Home_Garden_1",
    location = L_Home_Garden,
    label = "Label_Event_Garden_1",
    is_automatic = True, 
    unlock_condition = "E_Bathroom_Event_1.is_completed"
)
