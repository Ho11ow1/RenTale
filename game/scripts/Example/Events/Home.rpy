init offset = 1

default E_Bedroom_Event_1 = Event(
    name = "Home_Bedroom_Intro",
    location = L_Home_Bedroom,
    isUnlocked = True,
    isAutomatic = True,
    action = (
        "L_Home_Kitchen.Unlock();" 
        "E_Kitchen_Event_1.Unlock();"
    )
)

default E_Kitchen_Event_1 = Event(
    name = "Home_Kitchen_1",
    location = L_Home_Kitchen,
    isAutomatic = True, 
    unlockCondition = "E_Bedroom_Event_1.IsCompleted == True",
    action = (
        "L_Home_Bathroom.Unlock();" 
        "E_Bathroom_Event_1.Unlock();" 
        "renpy.call('Label_Event_Kitchen_1');"
    )
)

default E_Bathroom_Event_1 = Event(
    name = "Home_Bathroom_1",
    location = L_Home_Bathroom,
    isAutomatic = True,
    unlockCondition = "E_Kitchen_Event_1.IsCompleted == True",
    action = (
        "L_Home_Garden.Unlock();"
        "E_Garden_Event_1.Unlock();"
        "renpy.call('Label_Event_Bathroom_1');"
    )
)

default E_Garden_Event_1 = Event(
    name = "Home_Garden_1",
    location = L_Home_Garden,
    isAutomatic = True, 
    unlockCondition = "E_Bathroom_Event_1.IsCompleted == True",
    action = (
        "L_City_Main.Unlock();"
        "renpy.call('Label_Event_Garden_1');"
    )
)
