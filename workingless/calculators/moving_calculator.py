import datetime

from workingless.constants import MONDAY
from workingless.utils import get_next_day


class MovingCalculator:
    """
    Holidays calculation based in moving date if
    date isn't the specific date.
    For example: base date is january 6, if that date is not monday,
    holiday will be next monday.

    Args:
        month (int): base month
        day (int): base day
        next_day (int): next day to move holiday
    """

    __slots__ = ('_month', '_day', '_next_day')

    def __init__(self, month, day, next_day=MONDAY):
        self._month = month
        self._day = day
        self._next_day = next_day

    def calculate(self, year):
        """
        Calculate holiday from base date

        Args:
            year (int): year for calculate holiday

        Returns:
            datetime.date: holiday date
        """
        return get_next_day(date=datetime.date(year, self._month, self._day), next_day=self._next_day)
