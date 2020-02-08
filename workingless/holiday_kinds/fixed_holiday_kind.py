import datetime

from workingless import constants
from workingless.holiday_kind import HolidayKind


class FixedHolidayKind(HolidayKind):

    def get_kind(self):
        return constants.HolidayKindEnum.FIXED

    def calculate(self, year):
        return datetime.date(year, self._holiday.month, self._holiday.day)
