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

                        textbutton _("{b}Inventory{/b}"):
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

                    textbutton "✕":
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
                        use RenTale_dev_row("Is Morning:", TimeManager.IsMorning())
                        use RenTale_dev_row("Is Noon:", TimeManager.IsNoon())
                        use RenTale_dev_row("Is Afternoon:", TimeManager.IsAfternoon())
                        use RenTale_dev_row("Is Evening:", TimeManager.IsEvening())
                        use RenTale_dev_row("Is Night:", TimeManager.IsNight())

                        null height 4

                        use RenTale_dev_row("Is Day Time:", TimeManager.IsDaytime())
                        use RenTale_dev_row("Is Night Time:", TimeManager.IsNighttime())
                        use RenTale_dev_row("Is Weekday:", TimeManager.IsWeekday())
                        use RenTale_dev_row("Is Weekend:", TimeManager.IsWeekend())

                        null height 4

                        use RenTale_dev_row("Day Count:", TimeManager.GetDayCount())
                        use RenTale_dev_row("Week:", TimeManager.GetWeek())
                        use RenTale_dev_row("Day Name:", TimeManager.GetDayName())
                        use RenTale_dev_row("Time Of Day:", TimeManager.GetTimeOfDayName())


                    # ========================= LOCATIONS ========================= #
                    elif active_tab == 1:
                        for location in RenTale_All_Locations.keys():
                            use RenTale_dev_card(location.Name, [
                                ("Label:", location.Label),
                                ("Is Unlocked:", location.IsUnlocked)
                            ])


                    # ========================= EVENTS ========================= #
                    elif active_tab == 2:
                        for list in RenTale_All_Locations.values():
                            
                            null height 4

                            for event in list:
                                use RenTale_dev_card(event.Name, [
                                    ("Location:", event.Location.Name),
                                    ("Is Unlocked:", event.IsUnlocked),
                                    ("Is Automatic:", event.IsAutomatic),
                                    ("Is Completed:", event.IsCompleted),
                                    ("Unlock Condition:", event.UnlockCondition if event.UnlockCondition else "None"),
                                    ("Action:", event.Action if event.Action else "None")
                                ])
                                


                    # ========================= FLAGS ========================= #
                    elif active_tab == 3:
                        for name, flag in RenTale_All_Flags.items():
                            use RenTale_dev_row(f"{name}:", f"{flag.Value}")


                    # ========================= Inventory ========================= #
                    elif active_tab == 4:
                        for item in Inventory.Items:
                            use RenTale_dev_card(item.Name, [
                                    ("Quantity:", item.Quantity),
                                    ("Is Stackable:", item.IsStackable),
                                    ("Image:", item.Image if item.Image else "None"),
                                    ("Description:", item.Description)
                                ])


                    # ========================= ExtendedCharacters ========================= #
                    elif active_tab == 5:
                        for character in RenTale_All_Characters:
                            use RenTale_dev_card(character.Name, [
                                ("Relationship:", character.Relationship),
                                ("Friendship:", character.Friendship),
                                ("Love:", character.Love),
                                ("Lust:", character.Lust)
                            ])


                    # ========================= GALLERY ========================= #
                    elif active_tab == 6:
                        for gi in RenTale_Gallery_List:
                            use RenTale_dev_card(gi.Name, [
                                    ("Label:", gi.Label),
                                    ("Thumbnail:", gi.Thumbnail),
                                    ("Scope:", gi.Scope if gi.Scope else "{{}"),
                                    ("IsUnlocked:", gi.IsUnlocked)
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

                            if ';' in str(value):
                                $ arr = str(value).split(';')
                                $ formatted = "; \n".join(arr)
                                
                                text "[formatted]" style "RenTale_dev_card_kvp_value_text"

                            else:
                                text "[str(value).strip()]" style "RenTale_dev_card_kvp_value_text"

            frame:
                background RenTale_color_separator
                xfill True
                ysize 2
                padding (0, 0)
