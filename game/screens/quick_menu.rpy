init python:
    config.overlay_screens.append("quick_menu")


default quick_menu = True


screen quick_menu():
    zorder 100

    if quick_menu and persistent.quickmenu_enabled:

        hbox:
            style_prefix "quick"
            align (persistent.quickmenu_position_x, 1.0)

            if persistent.quickmenu_rollback_enabled:
                textbutton _("Back") action Rollback()
            if persistent.quickmenu_history_enabled:
                textbutton _("History") action ShowMenu("history")
            if persistent.quickmenu_skip_enabled:
                textbutton _("Skip") action Skip() alternate Skip(fast = True, confirm = True)
            if persistent.quickmenu_autosave_enabled:
                textbutton _("Auto") action Preference("auto-forward", "toggle")
            if persistent.quickmenu_save_enabled:
                textbutton _("Save") action ShowMenu("save")
            if persistent.quickmenu_quicksave_enabled:
                textbutton _("Q.Save") action QuickSave()
            if persistent.quickmenu_quicksave_enabled:
                textbutton _("Q.Load") action QuickLoad()
            if persistent.quickmenu_prefs_enabled:
                textbutton _("Prefs") action ShowMenu("preferences")


style quick_button is default:
    background Frame((["gui/phone/button/quick_[prefix_]background.png", "gui/phone/button/[prefix_]background.png"] if renpy.variant("small") else []) + ["gui/button/quick_[prefix_]background.png", "gui/button/[prefix_]background.png"], gui.quick_button_borders, tile = gui.button_tile)
    padding gui.quick_button_borders.padding

style quick_button_text is button_text:
    size gui.quick_button_text_size
    idle_color gui.quick_button_text_idle_color
    selected_color gui.quick_button_text_selected_color
