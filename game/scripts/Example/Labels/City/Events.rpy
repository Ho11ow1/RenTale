label Label_Event_Library_1:

    "You meet a mysterious girl reading a book in the corner of the library"

    menu:
        "Join her and talk":
            $ Willow.IncreaseStat(StatType.Friendship, 10)
            $ Willow.IncreaseStat(StatType.Love, 1)
            $ Willow.IncreaseStat(StatType.Lust, 2)

            "[Willow.Name] enjoyed your company but quickly left"


        "Wave and quickly leave":

            Willow "Hi..."

    $ GI_Willow_Meet.Unlock()

    return


label Label_Event_Park_1:

    "You meet a sweet girl sitting on a park bench alone"

    menu:
        "Join her and talk":
            $ Alice.IncreaseStat(StatType.Friendship, 5)
            $ Alice.IncreaseStat(StatType.Love, 2)

            "[Alice.Name] enjoyed your company and asked you to meet again"


        "Sit next to her in silence":
            $ Alice.IncreaseStat(StatType.Friendship, 2)

            Alice "Don't be nervous, i won't bite"

    $ GI_Alice_Meet.Unlock()

    return
