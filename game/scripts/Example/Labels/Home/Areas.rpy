label RenTale_Label_Example:

    call screen QTE_Simple()

    if _return:
        e "You clicked in time."
    else:
        e "You failed to click in time."

    e "Anyways, let's move on."

    show screen InventoryBSDisplay
    show screen TimeDisplay

    $ Player.name = renpy.input(default = "Calli", prompt = "What's your name?", length = 8).strip()

    $ rentale.go_to(L_Home_Bedroom)

    return


label Label_Home_Bedroom:

    $ rentale.trigger_automatic_events()

    "Something i guess"

    call screen LocationSelect


label Label_Home_Kitchen:

    $ rentale.trigger_automatic_events()

    "More of something"

    call screen LocationSelect


label Label_Home_Bathroom:

    $ rentale.trigger_automatic_events()

    "Almost everything"

    call screen LocationSelect


label Label_Home_Garden:

    $ rentale.trigger_automatic_events()

    "Everything"

    call screen LocationSelect
