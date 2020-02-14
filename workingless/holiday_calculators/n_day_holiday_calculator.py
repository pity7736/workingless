import datetime

from dateutil.relativedelta import relativedelta

from workingless.constants import MONDAY


class PositionDayHolidayCalculator:
    """
    Holidays calculation when holiday is position day of month.

    For example:
        - First monday of february
        - Third monday of march

    Args:
        month (int): month
        day (int): base day, usually first (1)
        position (int): position of the month
        weekday (int): day of week
    """

    __slots__ = ('_month', '_day', '_position', '_weekday')

    def __init__(self, month: int, day: int, position: int, weekday: int = MONDAY):
        self._month = month
        self._day = day
        self._position = position - 1
        self._weekday = weekday

    def calculate(self, year: int) -> datetime.date:
        """
        Calculate holiday based in position day of month

        Args:
            year (int): year for calculate holiday

        Returns:
            datetime.date: holiday date
        """
        base_date = datetime.date(year=year, month=self._month, day=self._day)
        first_date = base_date + relativedelta(weekday=self._weekday)
        return first_date + relativedelta(days=7 * self._position)
