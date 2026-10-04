init python:
    config.overlay_screens.append("quick_menu")


default quick_menu = True


screen quick_menu():
    zorder 100

    if quick_menu and persistent.quickmenu_enabled:

        hbox:
            style_prefix "quick"
            xalign persistent.quickmenu_position_x
            yalign 1.0

            if persistent.quickmenu_rollback_enabled :
                textbutton _("Back") action Rollback()
            if persistent.quickmenu_history_enabled:
                textbutton _("History") action ShowMenu('history')
            if persistent.quickmenu_skip_enabled:
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            if persistent.quickmenu_autosave_enabled:
                textbutton _("Auto") action Preference("auto-forward", "toggle")
            if persistent.quickmenu_save_enabled:
                textbutton _("Save") action ShowMenu('save')
            if persistent.quickmenu_quicksave_enabled:
                textbutton _("Q.Save") action QuickSave()
            if persistent.quickmenu_quicksave_enabled:
                textbutton _("Q.Load") action QuickLoad()
            if persistent.quickmenu_prefs_enabled:
                textbutton _("Prefs") action ShowMenu('preferences')


style quick_button is default:
    properties gui.button_properties("quick_button")

style quick_button_text is button_text:
    properties gui.text_properties("quick_button")
