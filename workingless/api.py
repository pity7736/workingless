import datetime
from typing import Union, Generator

from workingless import constants
from workingless.holiday import Holiday


holidays = (
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


def is_holiday(date: Union[datetime.date, datetime.datetime]) -> bool:
    """
    Validate if a date is a holiday

    Args:
        date (datetime.date, datetime.datetime): date to validate.

    Returns:
        bool: True if the date is holiday, False otherwise.

    """
    if isinstance(date, datetime.datetime):
        date = date.date()
    return date in get_holidays_from_year(date.year)


def get_holidays_from_year(year: int) -> Generator[datetime.date, None, None]:
    """
    Get holidays from a specific year

    Args:
        year (int): year

    Returns:
        Generator: holidays from that year.

    """
    for holiday in holidays:
        yield holiday.calculate(year=year)
