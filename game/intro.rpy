# ===================================================================================== #
#
# This label runs before the game starts, It should be used for intro cinematics
# If your game doesn't require a splashscreen, comment out the label below
#
# ===================================================================================== #
label splashscreen:

    return

# ===================================================================================== #
#
# This label runs just before the user sees the main menu, it's best used for initialization
# If your game doesn't need to do anything before main menu loads, comment out the label below
#
# ===================================================================================== #
label before_main_menu:
    $ Discord.Init()
    $ Discord.Update("", "")

    return
