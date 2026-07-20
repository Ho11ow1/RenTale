## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.

## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("RenTale")

## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "0.0.1"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "RenTale"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any
## other number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "RenTale"

## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"

## ADDITIONAL SETTINGS VARIABLES ##################################################
# region ADDITIONAL SETTINGS
# Set default config variables for a good starting point
define config.default_fullscreen = False
define config.has_autosave = True
define config.has_quicksave = True
define config.default_music_volume = 0.5
define config.default_sfx_volume = 0.5
define config.default_voice_volume = 0.5

# Variables that dictate the state of the quickmenu
default persistent.quickmenu_position_x = 0.0
default persistent.quickmenu_enabled = True
default persistent.quickmenu_rollback_enabled = True
default persistent.quickmenu_history_enabled = True
default persistent.quickmenu_skip_enabled = True
default persistent.quickmenu_autosave_enabled = True
default persistent.quickmenu_save_enabled = True
default persistent.quickmenu_quicksave_enabled = True
default persistent.quickmenu_quickload_enabled = True
default persistent.quickmenu_prefs_enabled = True

# Variables that dictate whether the game should have quick and auto save enabled along with accessing them via the file_slots screens | Does not disable manual invocations via the quickmenu
default persistent.has_autosave = True
default persistent.has_quicksave = True

# Variables which allow for moving across filepages above page 9
default persistent._file_chapter = 0

# Variables which allow for customising the textbox visuals
default persistent.textbox_opacity = 1.0
default persistent.textbox_height = 270
default persistent.textbox_width = 1130

# Quick python block to restore variables to persistent state on re-launch
init python:
    config.has_autosave = persistent.has_autosave
    config.has_quicksave = persistent.has_quicksave
    renpy.store.quick_menu = persistent.quickmenu_enabled
# endregion
## URL PROMO ##################################################################################################################
# region URL SELF PROMO
## TODO: UPDATE URL VARIABLES TO YOUR NEEDS | ELSE LEAVE AS NONE
## Updating these variables will display the appropriate icon aswell as handle opening the URL in the users browser. | See more in `screens.rpy - screen main_menu`.
## Additionally SubscribeStar is also supported however it is more rare and as such must be implemented personally. The process is just a simple copy paste.
define url_patreon = None
define url_discord = None
define url_hover_sound = None
# endregion
## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:
    def CreateRPAName(seed) -> str:
        rng = renpy.random.Random(seed)

        leftBits = list()
        rightBits = list()
        left = ""
        right = ""

        for i in range(8):
            leftBits.append(str(rng.randint(0, 1)))
            rightBits.append(str(rng.randint(0, 1)))

        left = "".join(leftBits)
        right = "".join(rightBits)

        return f"{left}_{right}"

    RenTaleRPA = CreateRPAName("rentale")
    ScriptsRPA = CreateRPAName("scripts")
    ImagesRPA = CreateRPAName("images")
    MoviesRPA = CreateRPAName("movies")
    AudioRPA = CreateRPAName("audio")
    GuiRPA = CreateRPAName("gui")
    LibsRPA = CreateRPAName("libs")
    PackagesRPA = CreateRPAName("python-packages")
    FontsRPA = CreateRPAName("fonts")

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory,
    ## "game/**.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    # ==============================
    # Remove junk & source files
    # ==============================
    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)
    build.classify("LICENSE", None)
    build.classify("README.md", None)
    build.classify("CREDITS.txt", None)
    build.classify("**.rpy", None)

    # ===============
    # Create RPAs
    # ===============
    build.archive(RenTaleRPA, "all")
    build.archive(ScriptsRPA, "all")
    build.archive(ImagesRPA, "all")
    build.archive(MoviesRPA, "all")
    build.archive(AudioRPA, "all")
    build.archive(GuiRPA, "all")
    build.archive(LibsRPA, "all")
    build.archive(PackagesRPA, "all")
    build.archive(FontsRPA, "all")

    # ===============
    # Classify specific files to be places into the RPA archives
    # ===============
    build.classify("game/RenTale/**", RenTaleRPA)
    build.classify("game/**.rpyc", ScriptsRPA)
    build.classify("game/images/**", ImagesRPA)
    build.classify("game/movies/**", MoviesRPA)
    build.classify("game/audio/**", AudioRPA)
    build.classify("game/gui/**", GuiRPA)
    build.classify("game/libs/**", LibsRPA)
    build.classify("game/python-packages/**", PackagesRPA)
    build.classify("game/fonts", FontsRPA)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    # ===============
    # Documentation
    # ===============
    build.documentation("*.html")
    build.documentation("*.txt")

## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
