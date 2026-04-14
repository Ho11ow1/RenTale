init offset = 1

default E_City_Unlock_All = Event(
    name = "Unlock_City",
    location = L_City_Main,
    isUnlocked = True,
    isAutomatic = True,
    action = (
        "L_City_Park.Unlock();"
        "L_City_Library.Unlock();"
    )
)

default E_Meet_Willow = Event(
    name = "Meet_Willow",
    location = L_City_Library,
    isUnlocked = True,
    action = (
        "WillowFlags.HaveMet.Set(True);"
        "renpy.call('Label_Event_Library_1');"
    )
)

default E_Meet_Alice = Event(
    name = "Meet_Alice",
    location = L_City_Park,
    isUnlocked = True,
    action = (
        "AliceFlags.HaveMet.Set(True);"
        "renpy.call('Label_Event_Park_1');"
    )
)
