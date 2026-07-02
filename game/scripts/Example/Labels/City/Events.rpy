label Label_Event_City_1:
    $ L_City_Park.unlock()
    $ L_City_Library.unlock()

    return


label Label_Event_Library_1:
    if not _in_replay:
        $ rentale.AudioManager.play_sound("audio/SFX/Notification.mp3"),

    "You meet a mysterious girl reading a book in the corner of the library"

    menu:
        "Join her and talk":
            $ Willow.increase_stat(StatType.Friendship, 10)
            $ Willow.increase_stat(StatType.Love, 1)
            $ Willow.increase_stat(StatType.Lust, 2)

            Willow "Oh uh... hi"
            Willow "I'm really sorry but i have to go or i'll be late, Bye!"


        "Wave and quickly leave":
            $ Willow.increase_stat(StatType.Friendship, 1)

            Willow "Hi..."


    $ GI_Willow_Meet.unlock()
    $ WillowFlags.HaveMet.set(True),

    return


label Label_Event_Park_1:
    if not _in_replay:
        $ rentale.AudioManager.play_sound("audio/SFX/Notification.mp3"),

    "You meet a sweet girl sitting on a park bench alone"

    menu:
        "Join her and talk":
            $ Alice.increase_stat(StatType.Friendship, 5)
            $ Alice.increase_stat(StatType.Love, 2)

            Alice "It was nice talking to you [Player.Name], Same time next week?"


        "Sit next to her in silence":
            $ Alice.increase_stat(StatType.Friendship, 2)

            Alice "Don't be nervous, i won't bite"


    $ GI_Alice_Meet.unlock()
    $ WillowFlags.HaveMet.set(True)

    return
