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
