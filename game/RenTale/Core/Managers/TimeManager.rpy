init -90 python:
    class TimeManager():
        @staticmethod
        def IsMorning() -> bool:
            """
            Returns true if the current time of day is "Morning"
            """
            return store.RenTale_time_of_day_num == 0

        @staticmethod
        def IsNoon() -> bool:
            """
            Returns true if the current time of day is "Noon"
            """
            return store.RenTale_time_of_day_num == 1

        @staticmethod
        def IsAfternoon() -> bool:
            """
            Returns true if the current time of day is "Afternoon"
            """
            return store.RenTale_time_of_day_num == 2

        @staticmethod
        def IsEvening() -> bool:
            """
            Returns true if the current time of day is "Evening"
            """
            return store.RenTale_time_of_day_num == 3

        @staticmethod
        def IsNight() -> bool:
            """
            Returns true if the current time of day is "Night"
            """
            return store.RenTale_time_of_day_num == 4

        @staticmethod
        def IsDaytime() -> bool:
            """
            Returns true if the current time of day is earlier than "Evening"
            """
            return store.RenTale_time_of_day_num < 3

        @staticmethod
        def IsNighttime() -> bool:
            """
            Returns true if the current time of day is later than "Afternoon"
            """
            return store.RenTale_time_of_day_num > 2

        @staticmethod
        def IsWeekday() -> bool:
            """
            Returns true if the current day is a week day
            """
            return RenTale_day_names.index(store.RenTale_day_name) not in RenTale_weekend_indexes

        @staticmethod
        def IsWeekend() -> bool:
            """
            Returns true if the current day is a weekend
            """
            return RenTale_day_names.index(store.RenTale_day_name) in RenTale_weekend_indexes

        @staticmethod
        def GetTimeOfDayName() -> str:
            """
            Returns the current time of days name
            """
            return store.RenTale_time_of_day_name

        @staticmethod
        def GetDayName() -> str:
            """
            Returns true current days name
            """
            return store.RenTale_day_name

        @staticmethod
        def GetDayCount() -> int:
            """
            Returns the amount of days that have passed since starting the game
            """
            return store.RenTale_day_count

        @staticmethod
        def GetWeek() -> int:
            """
            Returns the amount of weeks that have passed since starting the game
            """
            return store.RenTale_week
