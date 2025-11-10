init 1 python:
    from enum import Enum
    
    class TimeOfDay(Enum):
        Morning = 0
        Noon = 1
        Afternoon = 2
        Evening = 3
        Night = 4
        Midnight = 5

    class TimeManager:
        _daysOfWeek = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
        _weekendDays = [ "Saturday", "Sunday" ]
        
        DayPeriod = TimeOfDay.Morning
        Day = _daysOfWeek[0]
        DayCount = int(1)
        Week = int(1)
        IsWeekend = False

        @classmethod
        def AdvanceDayPeriod(cls):
            match cls.DayPeriod:
                case TimeOfDay.Morning:
                    cls.DayPeriod = TimeOfDay.Noon
                    return
                case TimeOfDay.Noon:
                    cls.DayPeriod = TimeOfDay.Afternoon
                    return
                case TimeOfDay.Afternoon:
                    cls.DayPeriod = TimeOfDay.Evening
                    return
                case TimeOfDay.Evening:
                    cls.DayPeriod = TimeOfDay.Night
                    return
                case TimeOfDay.Night:
                    cls.DayPeriod = TimeOfDay.Midnight
                    return
                case TimeOfDay.Midnight:
                    cls.DayPeriod = TimeOfDay.Morning
                    cls.AdvanceDay()
                    return


        @classmethod
        def SetDayPeriod(cls, period):
            if type(period) != TimeOfDay:
                raise TypeError("Parameter must be a TimeOfDay enum instance")

            cls.DayPeriod = period


        @classmethod
        def AdvanceDay(cls):
            previousDayIndex = cls._daysOfWeek.index(cls.Day)

            if previousDayIndex == len(cls._daysOfWeek) - 1:
                cls.Day = cls._daysOfWeek[0]
                cls.AdvanceWeek()
            else:
                cls.Day = cls._daysOfWeek[previousDayIndex + 1]

            cls.DayCount += 1
                
            cls.IsWeekend = cls.Day in cls._weekendDays


        @classmethod
        def SetDay(cls, index):
            if type(index) != int:
                raise TypeError(f"Expected int, got {type(index).__name__}")
            if index < 0 or index >= len(cls._daysOfWeek):
                raise ValueError(f"Day index '{index}' is outside the bounds of the _daysOfWeek array")
            
            cls.Day = cls._daysOfWeek[index]
            cls.IsWeekend = cls.Day in cls._weekendDays


        @classmethod
        def AdvanceWeek(cls):
            cls.Week += 1


        @classmethod
        def SetWeek(cls, value):
            if type(value) != int:
                raise TypeError(f"Expected int, got {type(value).__name__}")
            if value < 1:
                raise ValueError(f"Week must be positive, got {value}")

            cls.Week = value
