from dateutil.easter import easter
from dateutil.relativedelta import relativedelta

from workingless import constants
from workingless.holiday_kind import HolidayKind


class EasterHolidayKind(HolidayKind):

    def get_kind(self):
        return constants.HolidayKindEnum.EASTER

    def calculate(self, year):
        return easter(year) + relativedelta(days=self._holiday.days)
