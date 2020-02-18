import datetime
from typing import Optional


class EveryNYearsCalculator:

    def __init__(self, month: int, day: int, every: int):
        self._month = month
        self._day = day
        self._every = every

    def calculate(self, year: int) -> Optional[datetime.date]:
        if (2018 - year) % self._every == 0:
            return datetime.date(year, self._month, self._day)
