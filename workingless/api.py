import datetime
from typing import Union, Generator

from workingless import constants
from workingless.holiday_calculator import HolidayCalculator


holidays = (
    HolidayCalculator(constants.HolidayKind.FIXED, constants.JANUARY, 1),
    HolidayCalculator(constants.HolidayKind.MOVING, constants.JANUARY, 6),
    HolidayCalculator(constants.HolidayKind.MOVING, constants.MARCH, 19),
    HolidayCalculator(constants.HolidayKind.EASTER, days=-7),
    HolidayCalculator(constants.HolidayKind.EASTER, days=-3),
    HolidayCalculator(constants.HolidayKind.EASTER, days=-2),
    HolidayCalculator(constants.HolidayKind.EASTER, days=0),
    HolidayCalculator(constants.HolidayKind.FIXED, constants.MAY, 1),
    HolidayCalculator(constants.HolidayKind.EASTER, days=43),
    HolidayCalculator(constants.HolidayKind.EASTER, days=64),
    HolidayCalculator(constants.HolidayKind.EASTER, days=71),
    HolidayCalculator(constants.HolidayKind.MOVING, constants.JUNE, 29),
    HolidayCalculator(constants.HolidayKind.FIXED, constants.JULY, 20),
    HolidayCalculator(constants.HolidayKind.FIXED, constants.AUGUST, 7),
    HolidayCalculator(constants.HolidayKind.MOVING, constants.AUGUST, 15),
    HolidayCalculator(constants.HolidayKind.MOVING, constants.OCTOBER, 12),
    HolidayCalculator(constants.HolidayKind.MOVING, constants.NOVEMBER, 1),
    HolidayCalculator(constants.HolidayKind.MOVING, constants.NOVEMBER, 11),
    HolidayCalculator(constants.HolidayKind.FIXED, constants.DECEMBER, 8),
    HolidayCalculator(constants.HolidayKind.FIXED, constants.DECEMBER, 25),
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
