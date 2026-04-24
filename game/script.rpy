# ===================================================================================== #
#
# This label runs before the game starts, It should be used for intro cinematics
#
# ===================================================================================== #
# label splashscreen:

#     return

# The game starts here.
label start:
    $ AudioManager.PlayBGM("audio/BGM/Lofi.mp3", loop = True)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # =============== RenTale Example Starts Here =============== #
    jump RenTale_Label_Example

    # This ends the game.

    return
