import calendar
import datetime

from dateutil.relativedelta import relativedelta

from workingless.constants import MONDAY


class PositionDayCalculator:
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
        if position < 1 or position > 5:
            raise ValueError('position must be grater than 0 and less than 6')

        self._position = position
        self._weekday = weekday

    def calculate(self, year: int) -> datetime.date:
        """
        Calculate holiday based in position day of month

        Args:
            year (int): year for calculate holiday

        Returns:
            datetime.date: holiday date
        """
        monthcalendar = calendar.monthcalendar(year=year, month=self._month)
        number_days = len(tuple(filter(None, map(lambda week: week[0], monthcalendar))))
        if self._position > number_days:
            raise ValueError(f'position ({self._position}) is greater than number of days of this month: {number_days}')

        base_date = datetime.date(year=year, month=self._month, day=self._day)
        first_date = base_date + relativedelta(weekday=self._weekday)
        return first_date + relativedelta(days=7 * (self._position - 1))
