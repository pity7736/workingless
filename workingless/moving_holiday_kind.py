import datetime

from workingless import constants
from workingless.holiday_kind import HolidayKind
from workingless.utils import get_next_day


class MovingrHolidayKind(HolidayKind):

    def get_kind(self):
        return constants.HolidayKindEnum.MOVING

    def calculate(self, year):
        return get_next_day(datetime.date(year, self._holiday.month, self._holiday.day))
