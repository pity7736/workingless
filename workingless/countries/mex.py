from workingless import constants
from workingless.calculators import FixedCalculator, PositionDayCalculator, \
    EasterCalculator, EveryNYearsCalculator
from .country_base import CountryBase


class MEX(CountryBase):

    @staticmethod
    def _get_base_country_holidays():
        return (
            FixedCalculator(month=constants.JANUARY, day=1),
            PositionDayCalculator(month=constants.FEBRUARY, day=1, position=1, weekday=constants.MONDAY),
            PositionDayCalculator(month=constants.MARCH, day=1, position=3),
            EasterCalculator(days=-2),
            FixedCalculator(month=constants.MAY, day=1),
            FixedCalculator(month=constants.SEPTEMBER, day=16),
            PositionDayCalculator(month=constants.NOVEMBER, day=1, position=3),
            EveryNYearsCalculator(month=constants.DECEMBER, day=1, base_year=2018, every=6),
            FixedCalculator(month=constants.DECEMBER, day=25),
        )
