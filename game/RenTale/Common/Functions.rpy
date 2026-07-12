init python in rentale:
# ========================= MAP MOVEMENT ========================= # 
    def go_to(location: Location) -> None:
        """
        Navigates to the given location if it exists and is unlocked
        """
        if type(location) != Location:
            raise RenTaleTypeError(Location, type(location))
            
        if location in all_locations:
            if location.IsUnlocked:
                renpy.store.rentale.current_location = location
                renpy.jump(location.Label)


# ========================= EVENT HANDLING ========================= #
    def trigger_automatic_events() -> None:
        """
        Triggers all automatic events at the current location that are unlocked, pass their condition and have not been completed
        """
        for event in all_locations[current_location]:
            if event.IsCompleted:
                continue
            if event.IsUnlocked and event.IsAutomatic and event.check_condition():
                event.play()


# =========================  GALLERY HELPER ========================= #
    def generate_filtered_list(prefix: str) -> set:
        """
        Returns a filtered set of GalleryItems where the name starts with the given prefix
        """
        if type(prefix) != str:
            raise RenTaleTypeError(str, type(prefix))

        filtered = set()

        for item in gallery_list:
            if item.Name.startswith(prefix):
                filtered.add(item)

        return filtered


# ========================= TIME MANAGEMENT ========================= #
    def advance_time(count: int = 1) -> None:
        """
        Advances the time of day by 'count' periods. Automatically advances the day and week when necessary
        """
        if type(count) != int:
            raise RenTaleTypeError(int, type(count))

        length = len(time_of_day_names)
        for i in range(count):
            renpy.store.rentale.time_of_day_num = (time_of_day_num + 1) % length
            renpy.store.rentale.time_of_day_name = time_of_day_names[time_of_day_num]

            if (time_of_day_num == 0):
                advance_days(1)


    def advance_days(count: int = 1) -> None:
        if type(count) != int:
            raise RenTaleTypeError(int, type(count))

        length = len(day_names)
        for i in range(count):
            renpy.store.rentale.day_count += 1
            current_index = day_names.index(day_name)
            renpy.store.rentale.day_name = day_names[(current_index + 1) % length]

            if ((day_count - 1) % len(day_names)) == 0:
                advance_weeks(1)


    def advance_weeks(count: int = 1) -> None:
        if type(count) != int:
            raise RenTaleTypeError(int, type(count))

        for i in range(count):
            renpy.store.rentale.week += 1

# ========================= VALIDATION UTIL ========================= #
    def _sanitize_string(string: str | None) -> str | None:
        if string is not None and type(string) != str:
            raise RenTaleTypeError((str, type(None)), type(string))
        if string is None:
            return string

        forbiddenFound = _blacklisted_regex.search(string)
        if forbiddenFound:
            arr = string.split(';')
            lines = list()
            for s in arr:
                lines.append(f"  {s.strip()}")
                
            formatted = '\n'.join(lines)
            
            raise RenTaleArgumentException(f"Forbidden operation detected: '{forbiddenFound.group()}' at index '{forbiddenFound.start()}' \n{formatted}")

        return string


    def _calc_chapter(num: int) -> int:
        return (num - 1) // 10
