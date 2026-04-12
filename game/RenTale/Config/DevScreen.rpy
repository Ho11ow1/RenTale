screen RenTale_DevScreen:

    zorder 99
    tag DevScreenHud


    frame:
        xalign 1.0
        yalign 0.0

        background None
        padding (0, 0)

        textbutton "RenTale_DevScreen":
            action Show("RenTale_DeveloperPanel")
            background None
            hover_background None


screen RenTale_DeveloperPanel:

    modal True
    zorder 999
    tag DevScreenPanel

    add "#00000088"

    frame:
        xfill True
        yfill True

        vbox:
            spacing 14

            hbox:
                xfill True

                textbutton "X":
                    xalign 1.0
                    action Hide("RenTale_DeveloperPanel")
                    background None
                    hover_background None

            null height 4

            hbox:
                xfill True
                text _("DayCount: [Time.get_day_count()] | DayName: [Time.get_day_name()]")

            null height 4

            hbox:
                xfill True
                text _("DayPeriod: [Time.get_period_name()]")

            null height 4

            hbox:
                xfill True
                text _("Week: [Time.get_week()]")

            null height 4

            hbox:
                xfill True
                text _("IsWeekend: [Time.is_weekend()] | IsWeekday: [Time.is_weekday()]")

            null height 4


init 999 python:
    def RenTale_ShowDevScreen():
        if DevMode:
            renpy.show_screen("RenTale_DevScreen")

    config.start_callbacks.append(RenTale_ShowDevScreen)
    config.after_load_callbacks.append(RenTale_ShowDevScreen)
