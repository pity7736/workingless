import datetime

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta

from workingless.constants import HolidayKind
from workingless.utils import get_next_day


class HolidayCalculator:
    """
    Calculator for holidays.

    Take base date from month and day and calculate holiday.

    The ``days`` parameter is exclusive of ``month`` and ``day`` parameters.

    Args:
        kind (HolidayKind): kind of holiday
        month (int): base holiday month
        day (int): base holiday day
        days (int): this is specific for HolidayKing.EASTER. It's the relative days number from
                    easter date.

    Raises:
        AssertionError: when the all ``month``, ``day`` and ``days`` parameters have some data
    """

    __slots__ = ('_kind', '_month', '_day', '_days')

    def __init__(self, kind: HolidayKind, month: int = None, day: int = None, days: int = None):
        assert month and day or days is not None
        self._kind = kind
        self._month = month
        self._day = day
        self._days = days

    def calculate(self, year: int) -> datetime.date:
        """
        Calculate holiday from base date

        Args:
            year (int): year

        Returns:
            datetime.date: holiday date

        """
        if self._kind == HolidayKind.FIXED:
            return datetime.date(year, self._month, self._day)
        elif self._kind == HolidayKind.MOVING:
            return get_next_day(datetime.date(year, self._month, self._day))
        else:
            return easter(year) + relativedelta(days=self._days)
