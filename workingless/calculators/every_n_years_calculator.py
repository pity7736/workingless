import datetime
from typing import Optional


class EveryNYearsCalculator:
    """
    Holidays calculations based in every years from base year

    Args:
        month (int): month if every year is satisfied
        day (int): day if every year is satisfied
        base_year (int): base year for calculation
        every (int): how often
    """

    __slots__ = ('_month', '_day', '_base_year', '_every')

    def __init__(self, month: int, day: int, base_year: int, every: int):
        self._month = month
        self._day = day
        self._base_year = base_year
        self._every = every

    def calculate(self, year: int) -> Optional[datetime.date]:
        """
        It return base date if the ``year`` meets the condition

        Args:
            year (int): year for calculate holiday

        Returns:
            datetime.date: if year meets the condition, None otherwise.
        """
        if (self._base_year - year) % self._every == 0:
            return datetime.date(year, self._month, self._day)
