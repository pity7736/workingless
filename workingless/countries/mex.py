from workingless import constants
from workingless.holiday_calculators import FixedHolidayCalculator, PositionDayHolidayCalculator,\
    EasterHolidayCalculator
from .country_base import CountryBase


class MEX(CountryBase):

    @staticmethod
    def _get_base_country_holidays():
        return (
            FixedHolidayCalculator(month=constants.JANUARY, day=1),
            PositionDayHolidayCalculator(month=constants.FEBRUARY, day=1, position=1, weekday=constants.MONDAY),
            PositionDayHolidayCalculator(month=constants.MARCH, day=1, position=3),
            EasterHolidayCalculator(days=-2),
            FixedHolidayCalculator(month=constants.MAY, day=1),
            FixedHolidayCalculator(month=constants.SEPTEMBER, day=16),
            PositionDayHolidayCalculator(month=constants.NOVEMBER, day=1, position=3),
            FixedHolidayCalculator(month=constants.DECEMBER, day=25),
        )
