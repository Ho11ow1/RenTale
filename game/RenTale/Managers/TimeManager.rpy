init -90 python in rentale:
    class TimeManager():
        @staticmethod
        def is_morning() -> bool:
            """
            Returns true if the current time of day is "Morning"
            """
            return time_of_day_num == 0

        @staticmethod
        def is_noon() -> bool:
            """
            Returns true if the current time of day is "Noon"
            """
            return time_of_day_num == 1

        @staticmethod
        def is_afternoon() -> bool:
            """
            Returns true if the current time of day is "Afternoon"
            """
            return time_of_day_num == 2

        @staticmethod
        def is_evening() -> bool:
            """
            Returns true if the current time of day is "Evening"
            """
            return time_of_day_num == 3

        @staticmethod
        def is_night() -> bool:
            """
            Returns true if the current time of day is "Night"
            """
            return time_of_day_num == 4

        @staticmethod
        def is_daytime() -> bool:
            """
            Returns true if the current time of day is earlier than "Evening"
            """
            return time_of_day_num < 3

        @staticmethod
        def is_nighttime() -> bool:
            """
            Returns true if the current time of day is later than "Afternoon"
            """
            return time_of_day_num > 2

        @staticmethod
        def is_weekday() -> bool:
            """
            Returns true if the current day is a week day
            """
            return day_names.index(day_name) not in weekend_indexes

        @staticmethod
        def is_weekend() -> bool:
            """
            Returns true if the current day is a weekend
            """
            return day_names.index(day_name) in weekend_indexes

        @staticmethod
        def get_time_of_day_name() -> str:
            """
            Returns the current time of days name
            """
            return time_of_day_name

        @staticmethod
        def get_day_name() -> str:
            """
            Returns true current days name
            """
            return day_name

        @staticmethod
        def get_day_count() -> int:
            """
            Returns the amount of days that have passed since starting the game
            """
            return day_count

        @staticmethod
        def get_week() -> int:
            """
            Returns the amount of weeks that have passed since starting the game
            """
            return week
