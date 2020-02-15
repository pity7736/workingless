from workingless import constants
from workingless.calculators import FixedCalculator, MovingCalculator, EasterCalculator
from .country_base import CountryBase


class COL(CountryBase):

    @staticmethod
    def _get_base_country_holidays():
        return (
            FixedCalculator(month=constants.JANUARY, day=1),
            MovingCalculator(month=constants.JANUARY, day=6),
            MovingCalculator(month=constants.MARCH, day=19),
            EasterCalculator(days=-7),
            EasterCalculator(days=-3),
            EasterCalculator(days=-2),
            EasterCalculator(days=0),
            FixedCalculator(month=constants.MAY, day=1),
            EasterCalculator(days=43),
            EasterCalculator(days=64),
            EasterCalculator(days=71),
            MovingCalculator(month=constants.JUNE, day=29),
            FixedCalculator(month=constants.JULY, day=20),
            FixedCalculator(month=constants.AUGUST, day=7),
            MovingCalculator(month=constants.AUGUST, day=15),
            MovingCalculator(month=constants.OCTOBER, day=12),
            MovingCalculator(month=constants.NOVEMBER, day=1),
            MovingCalculator(month=constants.NOVEMBER, day=11),
            FixedCalculator(month=constants.DECEMBER, day=8),
            FixedCalculator(month=constants.DECEMBER, day=25),
        )
