screen LocationSelect():

    modal True

    frame:
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 10

            text "Where would you like to go?"
            for location in rentale.all_locations:
                if location.is_unlocked:
                    textbutton location.name action rentale.MoveTo(location)
