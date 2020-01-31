import datetime
from typing import Union

from workingless import constants
from workingless.models.holiday import Holiday


holidays = (
    Holiday(constants.HolidayKind.FIXED, constants.JANUARY, 1),
    Holiday(constants.HolidayKind.MOVING, constants.JANUARY, 6),
    Holiday(constants.HolidayKind.MOVING, constants.MARCH, 19),
    Holiday(constants.HolidayKind.EASTER, days=-7),
    Holiday(constants.HolidayKind.EASTER, days=-3),
    Holiday(constants.HolidayKind.EASTER, days=-2),
    Holiday(constants.HolidayKind.EASTER, days=0),
    Holiday(constants.HolidayKind.FIXED, constants.MAY, 1),
    Holiday(constants.HolidayKind.EASTER, days=43),
    Holiday(constants.HolidayKind.EASTER, days=64),
    Holiday(constants.HolidayKind.EASTER, days=71),
    Holiday(constants.HolidayKind.MOVING, constants.JUNE, 29),
    Holiday(constants.HolidayKind.FIXED, constants.JULY, 20),
    Holiday(constants.HolidayKind.FIXED, constants.AUGUST, 7),
    Holiday(constants.HolidayKind.MOVING, constants.AUGUST, 15),
    Holiday(constants.HolidayKind.MOVING, constants.OCTOBER, 12),
    Holiday(constants.HolidayKind.MOVING, constants.NOVEMBER, 1),
    Holiday(constants.HolidayKind.MOVING, constants.NOVEMBER, 11),
    Holiday(constants.HolidayKind.FIXED, constants.DECEMBER, 8),
    Holiday(constants.HolidayKind.FIXED, constants.DECEMBER, 25),
)


def is_holiday(date: Union[datetime.date, datetime.datetime]):
    if isinstance(date, datetime.datetime):
        date = date.date()
    return date in get_holidays_from_year(date.year)


def get_holidays_from_year(year: int):
    for holiday in holidays:
        yield holiday.calculate(year=year)
