label MeetWillow:
    Willow "Oh... I didn't expect anyone to find me here."

    $ FlagManager.Set(Flags.Willow.HaveMet, True)
    $ Willow.IncreaseStat(StatType.Friendship, 2)

    return


label MeetAlice:
    Alice "Don't look so frightened. I'm Alice."

    $ FlagManager.Set(Flags.Alice.HaveMet, True)
    $ Alice.IncreaseStat(StatType.Lust, 1)

    return


label Leave:
    Narrator "You decided to do nothing..."

    return

