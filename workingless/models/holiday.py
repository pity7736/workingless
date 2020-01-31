import datetime

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta

from workingless.constants import HolidayKind
from workingless.utils import get_next_day


class Holiday:

    def __init__(self, kind: HolidayKind, month: int = None, day: int = None, days: int = None):
        assert month and day or days is not None
        self._kind = kind
        self._month = month
        self._day = day
        self._days = days

    def calculate(self, year: int):
        if self._kind == HolidayKind.FIXED:
            return datetime.date(year, self._month, self._day)
        elif self._kind == HolidayKind.MOVING:
            return get_next_day(datetime.date(year, self._month, self._day))
        else:
            return easter(year) + relativedelta(days=self._days)
