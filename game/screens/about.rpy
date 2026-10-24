screen about():
    tag menu

    use game_menu(_("About"), scroll = "viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_text is gui_text

style about_label_text is gui_label_text:
    size gui.label_text_size
