init -10 python:
    from enum import Enum
    
    class TimeOfDay(Enum):
        Morning = 0
        Noon = 1
        Afternoon = 2
        Evening = 3
        Night = 4
        Midnight = 5


    class TimeManager:
        """
            Centralized singleton time management system with runtime type validation.

            Manages game time progression including day periods, days of the week, and week counting.
        """

        def __init__(self):
            self._daysOfWeek = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
            self._weekendDays = [ "Saturday", "Sunday" ]
            self.DayPeriod = TimeOfDay.Morning
            self.Day = self._daysOfWeek[0]
            self.DayCount = int(1)
            self.Week = int(1)
            self.IsWeekend = False


        def AdvanceDayPeriod(self) -> None:
            """
                Advances the current day period.
            """

            match self.DayPeriod:
                case TimeOfDay.Morning:
                    self.DayPeriod = TimeOfDay.Noon
                    return
                case TimeOfDay.Noon:
                    self.DayPeriod = TimeOfDay.Afternoon
                    return
                case TimeOfDay.Afternoon:
                    self.DayPeriod = TimeOfDay.Evening
                    return
                case TimeOfDay.Evening:
                    self.DayPeriod = TimeOfDay.Night
                    return
                case TimeOfDay.Night:
                    self.DayPeriod = TimeOfDay.Midnight
                    return
                case TimeOfDay.Midnight:
                    self.DayPeriod = TimeOfDay.Morning
                    self.AdvanceDay()
                    return


        def SetDayPeriod(self, period: TimeOfDay) -> None:
            """
                Sets the current day period.

                Args:
                    period (TimeOfDay): TimeOfDay enum based on which the current day period should be set.

                Raises:
                    TypeError: If period is not a TimeOfDay instance.
            """

            if type(period) != TimeOfDay:
                raise TypeError("Parameter must be a TimeOfDay enum instance")

            self.DayPeriod = period


        def AdvanceDay(self) -> None:
            """
                Advances the current day period.
            """

            previousDayIndex = self._daysOfWeek.index(self.Day)

            if previousDayIndex == len(self._daysOfWeek) - 1:
                self.Day = self._daysOfWeek[0]
                self.AdvanceWeek()
            else:
                self.Day = self._daysOfWeek[previousDayIndex + 1]

            self.DayCount += 1
                
            self.IsWeekend = self.Day in self._weekendDays


        def SetDay(self, index: int) -> None:
            """
                Sets the current day by it's index.

                Args:
                    index (int): The index based on which day should be set.

                Raises:
                    TypeError: If index is not an int instance.
                    ValueError: If index is < 0 or index >= 6.
            """

            if type(index) != int:
                raise TypeError(f"Expected int, got {type(index).__name__}")
            if index < 0 or index >= len(self._daysOfWeek):
                raise ValueError(f"Day index '{index}' is outside the bounds of the _daysOfWeek array")
            
            self.Day = self._daysOfWeek[index]
            self.IsWeekend = self.Day in self._weekendDays


        def AdvanceWeek(self) -> None:
            """
                Advances the current week number by 1.
            """

            self.Week += 1


        def SetWeek(self, value: int) -> None:
            """
                Sets the current week number.

                Args:
                    value (int): The week number to set the week to.

                Raises:
                    TypeError: If value is not an int instance.
                    ValueError: If value is less than 1.
            """

            if type(value) != int:
                raise TypeError(f"Expected int, got {type(value).__name__}")
            if value < 1:
                raise ValueError(f"Week must be positive, got {value}")

            self.Week = value

