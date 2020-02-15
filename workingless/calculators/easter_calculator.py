import datetime

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta


class EasterCalculator:
    """
    Holidays calculations based in easter date.
    The holiday could be n days +/- from easter date.

    Args:
        days (int): days of difference from easter date
    """

    __slots__ = ('_days',)

    def __init__(self, days: int):
        self._days = days

    def calculate(self, year: int) -> datetime.date:
        """
        It returns easter date +/- days passed in constructor.

        Args:
            year (int): year for calculate holiday

        Returns:
            datetime.date: holiday date
        """
        return easter(year) + relativedelta(days=self._days)
