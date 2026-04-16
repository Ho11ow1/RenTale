label Label_Event_Library_1:

    "You meet a mysterious girl reading a book in the corner of the library"

    menu:
        "Join her and talk":
            $ Willow.IncreaseStat(StatType.Friendship, 10)
            $ Willow.IncreaseStat(StatType.Love, 1)
            $ Willow.IncreaseStat(StatType.Lust, 2)

            Willow "Oh uh... hi"
            Willow "I'm really sorry but i have to go or i'll be late, Bye!"


        "Wave and quickly leave":
            $ Willow.IncreaseStat(StatType.Friendship, 1)

            Willow "Hi..."


    $ GI_Willow_Meet.Unlock()

    return


label Label_Event_Park_1:

    "You meet a sweet girl sitting on a park bench alone"

    menu:
        "Join her and talk":
            $ Alice.IncreaseStat(StatType.Friendship, 5)
            $ Alice.IncreaseStat(StatType.Love, 2)

            Alice "It was nice talking to you [Player.Name], Same time next week?"


        "Sit next to her in silence":
            $ Alice.IncreaseStat(StatType.Friendship, 2)

            Alice "Don't be nervous, i won't bite"


    $ GI_Alice_Meet.Unlock()

    return
