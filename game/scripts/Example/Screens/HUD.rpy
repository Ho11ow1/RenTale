screen InventoryBSDisplay():
    zorder 10

    vbox:
        xalign 1.0

        text "Wallet: [rentale.inventory.money]"
        for item in sorted(rentale.all_items, key = lambda item: item.name):
            vbox:
                text "[rentale.inventory.contains(item)] | [item.name] | [item.quantity] | [item.cost] | [item.is_stackable]"
                hbox:
                    textbutton "Buy ([2 if item.is_stackable else 1])" action rentale.BuyItem(item, 2 if item.is_stackable else 1)
                    textbutton "SELL (1)" action rentale.SellItem(item, 1)


screen TimeDisplay():
    zorder 10

    vbox:
        xalign 0.0
        
        text "Day Count: [rentale.TimeManager.get_day_count()]"
        text "Week: [rentale.TimeManager.get_week()]"
        text "Day: [rentale.TimeManager.get_day_name()]"
        text "Time Of Day: [rentale.TimeManager.get_time_of_day_name()]"
        text "Weekend / Weekday: ['Weekend' if rentale.TimeManager.is_weekend() else 'Weekday']"

        null height 4
        textbutton "Advance Time" action rentale.SkipTime()
