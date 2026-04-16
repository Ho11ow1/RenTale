label RenTale_Label_Example:

    $ Player.Name = renpy.input(default = "Calli", prompt = "What's your name?", length = 8).strip()

    $ RenTale_GoTo(L_Home_Bedroom)

    return


label Label_Home_Bedroom:

    $ RenTale_TriggerAutomaticEvents()

    "Something i guess"

    call screen LocationSelect


label Label_Home_Kitchen:

    $ RenTale_TriggerAutomaticEvents()

    "More of something"

    call screen LocationSelect


label Label_Home_Bathroom:

    $ RenTale_TriggerAutomaticEvents()

    "Almost everything"

    call screen LocationSelect


label Label_Home_Garden:

    $ RenTale_TriggerAutomaticEvents()

    "Everything"

    call screen LocationSelect
