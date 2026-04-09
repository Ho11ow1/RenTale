init python:
# ========================= MAP MOVEMENT ========================= # 
    def RenTale_GoTo(location: Location) -> None:
        if type(location) != Location:
            raise TypeError(f"Expected 'Location', got '{type(location).__name__}'")
            
        if location in RenTale_ALL_LOCATIONS:
            if location.IsUnlocked:
                store.RenTale_CURRENT_LOCATION = location
                renpy.jump(location.Label)


# ========================= EVENT HANDLING ========================= #
    def RenTale_TriggerAutomaticEvents() -> None:
        for event in RenTale_ALL_LOCATIONS.get(store.RenTale_CURRENT_LOCATION, []):
            if event.IsCompleted:
                continue
            if event.IsUnlocked and event.IsAutomatic and event.CheckCondition():
                event.Play()


# ========================= TIME MANAGEMENT ========================= #
    def RenTale_advance_time(count: int = 1):
        if type(count) != int:
            raise TypeError(f"Expected 'Int', got '{type(count).__name__}'")

        length = len(RenTale_time_of_day_names)
        for _ in range(count):
            store.RenTale_time_of_day_num = (store.RenTale_time_of_day_num + 1) % length
            store.RenTale_time_of_day_name = RenTale_time_of_day_names[store.RenTale_time_of_day_num]

            if (store.RenTale_time_of_day_num == 0):
                RenTale_advance_days(1)


    def RenTale_advance_days(count: int = 1):
        if type(count) != int:
            raise TypeError(f"Expected 'Int', got '{type(count).__name__}'")

        length = len(RenTale_day_names)
        for _ in range(count):
            store.RenTale_day_count += 1
            current_index = RenTale_day_names.index(store.RenTale_day_name)
            store.RenTale_day_name = RenTale_day_names[(current_index + 1) % length]

            if ((store.RenTale_day_count - 1) % RenTale_days_per_week) == 0:
                RenTale_advance_weeks(1)


    def RenTale_advance_weeks(count: int = 1):
        if type(count) != int:
            raise TypeError(f"Expected 'Int', got '{type(count).__name__}'")

        for _ in range(count):
            store.RenTale_week += 1
