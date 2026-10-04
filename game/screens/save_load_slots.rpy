screen save():

    tag menu

    use file_slots(_(""))


screen load():

    tag menu

    use file_slots(_(""))


screen file_slots(title):

    # default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:
            ## This ensures the input will get the enter event before any of
            ## the buttons do.
            # order_reverse True

            ## The page name, which can be edited by clicking on a button.
            # button:
            #     style "page_label"

            #     key_events True
            #     xalign 0.5
            #     action page_name_value.Toggle()

            #     input:
            #         style "page_label_text"
            #         value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                align (0.5, 0.1)
                xoffset -200

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        vbox:

                            add FileScreenshot(slot) xalign 0.5

                            text FileTime(slot, format=_("%B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"
                                color gui.idle_color
                                hover_color gui.hover_color
                                selected_color gui.accent_color

                            text FileSaveName(slot):
                                style "slot_name_text"

                            key "save_delete" action FileDelete(slot)

            vbox:
                style_prefix "page"

                align (0.5, 1.0)
                xoffset -200

                key "save_page_prev" action FilePagePrevious()
                key "save_page_next" action FilePageNext()

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    hbox:
                        xalign 0.5
                        spacing 25

                        textbutton _("<<"):
                            text_style "custom_menu_btn"
                            text_kerning -3.5
                            action rentale.FilePageJump(step = -10)

                        textbutton _("<"):
                            text_style "custom_menu_btn"
                            action rentale.FilePageJump(step = -1)

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto"):
                            text_style "custom_menu_btn"

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick"):
                            text_style "custom_menu_btn"

                    for page in range((persistent._file_chapter * 10) + 1, (persistent._file_chapter * 10) + 11):
                        textbutton "[page]" action FilePage(page):
                            text_style "custom_menu_btn"

                    hbox:
                        textbutton _(">"):
                            text_style "custom_menu_btn"
                            action rentale.FilePageJump(step = 1)

                        textbutton _(">>"):
                            text_style "custom_menu_btn"
                            text_kerning -3.5
                            action rentale.FilePageJump(step = 10)

                # if config.has_sync:
                #     if CurrentScreenName() == "save":
                #         textbutton _("Upload Sync"):
                #             action UploadSync()
                #             xalign 0.5
                #     else:
                #         textbutton _("Download Sync"):
                #             action DownloadSync()
                #             xalign 0.5



style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label is gui_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text is gui_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button is gui_button:
    properties gui.button_properties("page_button")

style page_button_text is gui_button_text:
    properties gui.text_properties("page_button")

style slot_button is gui_button:
    properties gui.button_properties("slot_button")

style slot_button_text is gui_button_text:
    properties gui.text_properties("slot_button")
