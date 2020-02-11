import datetime

from workingless.constants import HolidayKindEnum
from workingless.holiday_calculators import EasterHolidayCalculator, FixedHolidayCalculator, MovingHolidayCalculator


class Holiday:
    """
    Calculator for holidays.

    Take base date from month and day and calculate holiday.

    The ``days`` parameter is exclusive of ``month`` and ``day`` parameters.

    Args:
        kind (HolidayKindEnum): kind of holiday
        month (int): base holiday month
        day (int): base holiday day
        days (int): this is specific for HolidayKing.EASTER. It's the relative days number from
                    easter date.

    Raises:
        AssertionError: when the all ``month``, ``day`` and ``days`` parameters have some data
    """

    __slots__ = ('_calculator', '_month', '_day', '_days')

    def __init__(self, kind: HolidayKindEnum, month: int = None, day: int = None, days: int = None):
        assert month and day or days is not None
        if kind == HolidayKindEnum.MOVING:
            self._calculator = MovingHolidayCalculator(self)
        elif kind == HolidayKindEnum.FIXED:
            self._calculator = FixedHolidayCalculator(self)
        else:
            self._calculator = EasterHolidayCalculator(self)
        self._month = month
        self._day = day
        self._days = days

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    @property
    def days(self):
        return self._days

    def calculate(self, year: int) -> datetime.date:
        """
        Calculate holiday from base date

        Args:
            year (int): year

        Returns:
            datetime.date: holiday date

        """
        return self._calculator.calculate(year)
