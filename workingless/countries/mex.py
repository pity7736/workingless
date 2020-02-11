from workingless import constants
from workingless.holiday import Holiday
from .country_base import CountryBase


class MEX(CountryBase):

    @staticmethod
    def _get_base_country_holidays():
        return (
            Holiday(constants.HolidayKindEnum.FIXED, constants.JANUARY, 1),
            Holiday(constants.HolidayKindEnum.FIXED, constants.MAY, 1),
            Holiday(constants.HolidayKindEnum.FIXED, constants.SEPTEMBER, 16),
            Holiday(constants.HolidayKindEnum.FIXED, constants.DECEMBER, 25),
        )
