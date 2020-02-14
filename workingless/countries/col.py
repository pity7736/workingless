from workingless import constants
from workingless.holiday_calculators import FixedHolidayCalculator, MovingHolidayCalculator, EasterHolidayCalculator
from .country_base import CountryBase


class COL(CountryBase):

    @staticmethod
    def _get_base_country_holidays():
        return (
            FixedHolidayCalculator(month=constants.JANUARY, day=1),
            MovingHolidayCalculator(month=constants.JANUARY, day=6),
            MovingHolidayCalculator(month=constants.MARCH, day=19),
            EasterHolidayCalculator(days=-7),
            EasterHolidayCalculator(days=-3),
            EasterHolidayCalculator(days=-2),
            EasterHolidayCalculator(days=0),
            FixedHolidayCalculator(month=constants.MAY, day=1),
            EasterHolidayCalculator(days=43),
            EasterHolidayCalculator(days=64),
            EasterHolidayCalculator(days=71),
            MovingHolidayCalculator(month=constants.JUNE, day=29),
            FixedHolidayCalculator(month=constants.JULY, day=20),
            FixedHolidayCalculator(month=constants.AUGUST, day=7),
            MovingHolidayCalculator(month=constants.AUGUST, day=15),
            MovingHolidayCalculator(month=constants.OCTOBER, day=12),
            MovingHolidayCalculator(month=constants.NOVEMBER, day=1),
            MovingHolidayCalculator(month=constants.NOVEMBER, day=11),
            FixedHolidayCalculator(month=constants.DECEMBER, day=8),
            FixedHolidayCalculator(month=constants.DECEMBER, day=25),
        )
