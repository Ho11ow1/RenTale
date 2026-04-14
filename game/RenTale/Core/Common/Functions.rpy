init python:
# ========================= MAP MOVEMENT ========================= # 
    def RenTale_GoTo(location: Location) -> None:
        """
        Navigates to the given location if it exists and is unlocked
        """
        if type(location) != Location:
            raise RenTaleTypeError(Location, type(location))
            
        if location in RenTale_All_Locations:
            if location.IsUnlocked:
                store.RenTale_Current_Location = location
                renpy.jump(location.Label)


# ========================= EVENT HANDLING ========================= #
    def RenTale_TriggerAutomaticEvents() -> None:
        """
        Triggers all automatic events at the current location that are unlocked, pass their condition and have not been completed
        """
        for event in RenTale_All_Locations.get(store.RenTale_Current_Location, []):
            if event.IsCompleted:
                continue
            if event.IsUnlocked and event.IsAutomatic and event.CheckCondition():
                event.Play()


# =========================  GALLERY HELPER ========================= #
    def RenTale_Generate_Filtered_List(prefix: str) -> set:
        """
        Returns a filtered set of GalleryItems where the name starts with the given prefix
        """
        if type(prefix) != str:
            raise RenTaleTypeError(str, type(prefix))

        filtered = set()

        for item in RenTale_Gallery_List:
            if item.Name.startswith(prefix):
                filtered.add(item)

        return filtered


# ========================= TIME MANAGEMENT ========================= #
    def RenTale_Advance_Time(count: int = 1):
        """
        Advances the time of day by 'count' periods. Automatically advances the day and week when necessary
        """
        if type(count) != int:
            raise RenTaleTypeError(int, type(count))

        length = len(RenTale_time_of_day_names)
        for _ in range(count):
            store.RenTale_time_of_day_num = (store.RenTale_time_of_day_num + 1) % length
            store.RenTale_time_of_day_name = RenTale_time_of_day_names[store.RenTale_time_of_day_num]

            if (store.RenTale_time_of_day_num == 0):
                RenTale_advance_days(1)


    def RenTale_advance_days(count: int = 1):
        if type(count) != int:
            raise RenTaleTypeError(int, type(count))

        length = len(RenTale_day_names)
        for _ in range(count):
            store.RenTale_day_count += 1
            current_index = RenTale_day_names.index(store.RenTale_day_name)
            store.RenTale_day_name = RenTale_day_names[(current_index + 1) % length]

            if ((store.RenTale_day_count - 1) % RenTale_days_per_week) == 0:
                RenTale_advance_weeks(1)


    def RenTale_advance_weeks(count: int = 1):
        if type(count) != int:
            raise RenTaleTypeError(int, type(count))

        for _ in range(count):
            store.RenTale_week += 1
