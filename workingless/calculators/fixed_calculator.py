import datetime


class FixedCalculator:
    """
    This is the simpliest implementation.
    It returns exactly the same date.

    Args:
        month: month
        day: day
    """

    __slots__ = ('_month', '_day')

    def __init__(self, month: int, day: int):
        self._month = month
        self._day = day

    def calculate(self, year: int) -> datetime.date:
        """
        It returns exactly the same date given.

        Args:
            year (int): year for calculate holiday

        Returns:
            datetime.date: holiday date
        """
        return datetime.date(year, self._month, self._day)
