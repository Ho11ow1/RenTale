label Label_Event_Bedroom_1:
    $ L_Home_Kitchen.unlock()
    $ E_Kitchen_Event_1.unlock()

    return


label Label_Event_Kitchen_1:
    $ moneyFound = 10

    Narrator "Not sure what kind of magic is happening here but i guess the bathroom is now available"

    $ rentale.inventory.money_gain(moneyFound)

    Narrator "You found $[moneyFound] left by your mom on the counter. Current wallet: [rentale.inventory.money]"

    $ L_Home_Bathroom.unlock()
    $ E_Bathroom_Event_1.unlock()

    return


label Label_Event_Bathroom_1:
    $ moneyFound = 5

    Narrator "Not sure what kind of magic is happening here but i guess the garden is now available"

    $ rentale.inventory.money_gain(moneyFound)

    Narrator "You found $[moneyFound] sitting on the counter. Current wallet: [rentale.inventory.money]"

    $ L_Home_Garden.unlock()
    $ E_Garden_Event_1.unlock()

    return


label Label_Event_Garden_1:
    $ moneyFound = 10

    Narrator "Nothing special happens here... Yet"

    $ rentale.inventory.money_gain(moneyFound)

    Narrator "You found $[moneyFound] hidden in the bushes. Current wallet: [rentale.inventory.money]"

    $ L_City_Main.unlock()
    $ rentale.inventory.item_gain(II_Apple, 2)

    return
