screen RenTale_DevScreen():

    zorder 99
    tag RenTale_Dev_Screen_Hud

    frame:
        background None
        padding (0, 0)
        align (1.0, 1.0)
        offset (-5, -5)

        textbutton _("DEV"):
            style "RenTale_dev_hud_button"
            action Show("RenTale_DeveloperPanel")


screen RenTale_DeveloperPanel():

    modal True
    zorder 999
    tag RenTale_Dev_Screen_Panel

    add RenTale_color_bg_dim

    default active_tab = 0

    frame:
        style "RenTale_dev_panel_frame"

        vbox:
            frame:
                style "RenTale_dev_topbar_frame"

                # ========================= NAV BAR ========================= #
                hbox:
                    xfill True

                    hbox:

                        textbutton _("{b}Time{/b}"):
                            style "RenTale_dev_tab_button"
                            selected (active_tab == 0)
                            action SetScreenVariable("active_tab", 0)

                        textbutton _("{b}Locations{/b}"):
                            style "RenTale_dev_tab_button"
                            selected (active_tab == 1)
                            action SetScreenVariable("active_tab", 1)

                        textbutton _("{b}Events{/b}"):
                            style "RenTale_dev_tab_button"
                            selected (active_tab == 2)
                            action SetScreenVariable("active_tab", 2)

                        textbutton _("{b}Flags{/b}"):
                            style "RenTale_dev_tab_button"
                            selected (active_tab == 3)
                            action SetScreenVariable("active_tab", 3)

                        textbutton _("{b}InventoryItems{/b}"):
                            style "RenTale_dev_tab_button"
                            selected (active_tab == 4)
                            action SetScreenVariable("active_tab", 4)

                        textbutton _("{b}Characters{/b}"):
                            style "RenTale_dev_tab_button"
                            selected (active_tab == 5)
                            action SetScreenVariable("active_tab", 5)

                        textbutton _("{b}Gallery{/b}"):
                            style "RenTale_dev_tab_button"
                            selected (active_tab == 6)
                            action SetScreenVariable("active_tab", 6)

                    null:
                        xfill True

                    textbutton "X":
                        style "RenTale_dev_close_button"
                        action Hide("RenTale_DeveloperPanel")

            frame:
                background RenTale_color_separator
                xfill True
                ysize 2
                padding (0, 0)

            # ========================= SCROLL LIST ========================= #
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                yinitial 0.0

                vbox:
                    spacing 1

                    # ========================= TIME SYSTEM ========================= #
                    if active_tab == 0:
                        use RenTale_dev_row("Is Morning:", rentale.TimeManager.is_morning())
                        use RenTale_dev_row("Is Noon:", rentale.TimeManager.is_noon())
                        use RenTale_dev_row("Is Afternoon:", rentale.TimeManager.is_afternoon())
                        use RenTale_dev_row("Is Evening:", rentale.TimeManager.is_evening())
                        use RenTale_dev_row("Is Night:", rentale.TimeManager.is_night())

                        null height 4

                        use RenTale_dev_row("Is Day Time:", rentale.TimeManager.is_daytime())
                        use RenTale_dev_row("Is Night Time:", rentale.TimeManager.is_nighttime())
                        use RenTale_dev_row("Is Weekday:", rentale.TimeManager.is_weekday())
                        use RenTale_dev_row("Is Weekend:", rentale.TimeManager.is_weekend())

                        null height 4

                        use RenTale_dev_row("Day Count:", rentale.TimeManager.get_day_count())
                        use RenTale_dev_row("Week:", rentale.TimeManager.get_week())
                        use RenTale_dev_row("Day Name:", rentale.TimeManager.get_day_name())
                        use RenTale_dev_row("Time Of Day:", rentale.TimeManager.get_time_of_day_name())


                    # ========================= LOCATIONS ========================= #
                    elif active_tab == 1:
                        for location in sorted(rentale.all_locations.keys(), key = lambda l: l.name):
                            use RenTale_dev_card(location.name, [
                                ("Label:", location.label),
                                ("Is Unlocked:", location.is_unlocked),
                                ("Events:", [event.name for event in rentale.all_locations[location]])
                            ])


                    # ========================= EVENTS ========================= #
                    elif active_tab == 2:
                        for list in rentale.all_locations.values():
                            
                            null height 4

                            for event in sorted(list, key = lambda e: e.name):
                                use RenTale_dev_card(event.name, [
                                    ("Location:", event.location.name),
                                    ("Label:", event.label),
                                    ("Is Unlocked:", event.is_unlocked),
                                    ("Is Automatic:", event.is_automatic),
                                    ("Is Completed:", event.is_completed),
                                    ("Unlock Condition:", event.unlock_condition if event.unlock_condition else "None"),
                                ])
                                


                    # ========================= FLAGS ========================= #
                    elif active_tab == 3:
                        for name, flag in sorted(rentale.all_flags.items(), key = lambda n: n):
                            use RenTale_dev_row(f"{name}:", f"{flag.value}")


                    # ========================= InventoryItems ========================= #
                    elif active_tab == 4:
                        for item in sorted(rentale.all_items, key = lambda item: item.name):
                            use RenTale_dev_card(item.name, [
                                    ("In Inventory:", rentale.inventory.contains(item)),
                                    ("Quantity:", item.quantity),
                                    ("Is Stackable:", item.is_stackable),
                                    ("Image:", item.image if item.image else "None"),
                                    ("Description:", item.description),
                                    ("Cost:", item.cost)
                                ])


                    # ========================= ExtendedCharacters ========================= #
                    elif active_tab == 5:
                        for character in sorted(rentale.all_characters, key = lambda c: c.name):
                            use RenTale_dev_card(character.name, [
                                ("Color:", character.color),
                                ("TextColor:", character.what_color),
                                ("Relationship:", character.relationship),
                                ("Note:", character.note),
                                ("Friendship:", character.friendship),
                                ("Love:", character.love),
                                ("Lust:", character.lust)
                            ])


                    # ========================= GALLERY ========================= #
                    elif active_tab == 6:
                        for gi in sorted(rentale.gallery_list, key = lambda gi: gi.name):
                            use RenTale_dev_card(gi.name, [
                                    ("Label:", gi.label),
                                    ("Image:", gi.image),
                                    ("Scope:", gi.scope if gi.scope else "{{}"),
                                    ("Is Unlocked:", gi.is_unlocked)
                                ])


# ========================= SIMPLE ROW (Time, Flags) ========================= #
screen RenTale_dev_row(label, value):
    frame:
        style "RenTale_dev_row_frame"
        padding (0, 0)

        vbox:
            xfill True

            hbox:
                frame:
                    style "empty"
                    xsize 160 
                    
                    text "[label]" style "RenTale_dev_row_label_text"

                text "[str(value)]" style "RenTale_dev_row_value_text"

            # separator line
            frame:
                background RenTale_color_separator
                xfill True
                ysize 2
                padding (0, 0)


# ========================= CARD ROW (Events, Locations, etc.) ========================= #
screen RenTale_dev_card(name, kvp_list):
    $ listHeight = len(kvp_list) * 18
    frame:
        style "RenTale_dev_card_frame"

        vbox:

            text "[name]" style "RenTale_dev_card_header_text"

            hbox:
                xfill True
                spacing 5

                frame:
                    xsize 3
                    ymaximum listHeight
                    background RenTale_color_accent_primary
                    padding (0, 0)

                vbox:
                    xfill True
                    spacing 0
                    for key, value in kvp_list:
                        hbox:
                            frame:
                                style "empty"
                                xsize 160

                                text "[key.strip()]" style "RenTale_dev_card_kvp_label_text"

                            if type(value) == dict:
                                vbox:
                                    $ joined = ", ".join(f"{k} | {v}" for k, v in value.items())
                                    text "[joined]" style "RenTale_dev_card_kvp_value_text"
                            
                            else:
                                text "[str(value).strip()]" style "RenTale_dev_card_kvp_value_text"

            frame:
                background RenTale_color_separator
                xfill True
                ysize 2
                padding (0, 0)
