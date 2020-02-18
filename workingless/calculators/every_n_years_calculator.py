import datetime
from typing import Optional


class EveryNYearsCalculator:

    __slots__ = ('_month', '_day', '_base_year', '_every')

    def __init__(self, month: int, day: int, base_year: int, every: int):
        self._month = month
        self._day = day
        self._base_year = base_year
        self._every = every

    def calculate(self, year: int) -> Optional[datetime.date]:
        if (self._base_year - year) % self._every == 0:
            return datetime.date(year, self._month, self._day)
