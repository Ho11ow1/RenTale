init -90 python:
    class TimeManager():
        @staticmethod
        def IsMorning() -> bool:
            return store.RenTale_time_of_day_num == 0

        @staticmethod
        def IsNoon() -> bool:
            return store.RenTale_time_of_day_num == 1

        @staticmethod
        def IsAfternoon() -> bool:
            return store.RenTale_time_of_day_num == 2

        @staticmethod
        def IsEvening() -> bool:
            return store.RenTale_time_of_day_num == 3

        @staticmethod
        def IsNight() -> bool:
            return store.RenTale_time_of_day_num == 4

        @staticmethod
        def IsDaytime() -> bool:
            return store.RenTale_time_of_day_num < 3

        @staticmethod
        def IsNighttime() -> bool:
            return store.RenTale_time_of_day_num > 2

        @staticmethod
        def IsWeekday() -> bool:
            return RenTale_day_names.index(store.RenTale_day_name) not in RenTale_weekend_indexes

        @staticmethod
        def IsWeekend() -> bool:
            return RenTale_day_names.index(store.RenTale_day_name) in RenTale_weekend_indexes

        @staticmethod
        def GetTimeOfDayName() -> str:
            return store.RenTale_time_of_day_name

        @staticmethod
        def GetDayName() -> str:
            return store.RenTale_day_name

        @staticmethod
        def GetDayCount() -> int:
            return store.RenTale_day_count

        @staticmethod
        def GetWeek() -> int:
            return store.RenTale_week
