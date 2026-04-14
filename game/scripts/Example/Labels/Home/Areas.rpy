label RenTale_Label_Example:

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


screen LocationSelect():

    modal True

    frame:
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 10

            text "Where would you like to go?"
            for location in RenTale_All_Locations:
                if location.IsUnlocked:
                    textbutton location.Name action MoveTo(location)
