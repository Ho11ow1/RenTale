label Label_Event_Kitchen_1:

    $ moneyFound = 10

    Narrator "Not sure what kind of magic is happening here but i guess the bathroom is now available"

    $ Player_Money.Receive(10)

    Narrator "You found $[moneyFound] left by your mom on the counter. Current wallet: [Player_Money.Quantity]"

    return


label Label_Event_Bathroom_1:

    $ moneyFound = 5

    Narrator "Not sure what kind of magic is happening here but i guess the garden is now available"

    $ Player_Money.Receive(5)

    Narrator "You found $[moneyFound] sitting on the counter. Current wallet: [Player_Money.Quantity]"

    return


label Label_Event_Garden_1:

    $ moneyFound = 10

    Narrator "Nothing special happens here... Yet"

    $ Player_Money.Receive(10)

    Narrator "You found $[moneyFound] hidden in the bushes. Current wallet: [Player_Money.Quantity]"

    return
