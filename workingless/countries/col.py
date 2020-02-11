from workingless import constants
from workingless.holiday import Holiday
from .country_base import CountryBase


class COL(CountryBase):

    @staticmethod
    def _get_base_country_holidays():
        return (
            Holiday(constants.HolidayKindEnum.FIXED, constants.JANUARY, 1),
            Holiday(constants.HolidayKindEnum.MOVING, constants.JANUARY, 6),
            Holiday(constants.HolidayKindEnum.MOVING, constants.MARCH, 19),
            Holiday(constants.HolidayKindEnum.EASTER, days=-7),
            Holiday(constants.HolidayKindEnum.EASTER, days=-3),
            Holiday(constants.HolidayKindEnum.EASTER, days=-2),
            Holiday(constants.HolidayKindEnum.EASTER, days=0),
            Holiday(constants.HolidayKindEnum.FIXED, constants.MAY, 1),
            Holiday(constants.HolidayKindEnum.EASTER, days=43),
            Holiday(constants.HolidayKindEnum.EASTER, days=64),
            Holiday(constants.HolidayKindEnum.EASTER, days=71),
            Holiday(constants.HolidayKindEnum.MOVING, constants.JUNE, 29),
            Holiday(constants.HolidayKindEnum.FIXED, constants.JULY, 20),
            Holiday(constants.HolidayKindEnum.FIXED, constants.AUGUST, 7),
            Holiday(constants.HolidayKindEnum.MOVING, constants.AUGUST, 15),
            Holiday(constants.HolidayKindEnum.MOVING, constants.OCTOBER, 12),
            Holiday(constants.HolidayKindEnum.MOVING, constants.NOVEMBER, 1),
            Holiday(constants.HolidayKindEnum.MOVING, constants.NOVEMBER, 11),
            Holiday(constants.HolidayKindEnum.FIXED, constants.DECEMBER, 8),
            Holiday(constants.HolidayKindEnum.FIXED, constants.DECEMBER, 25),
        )
