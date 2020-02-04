from enum import Enum

MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = range(7)

JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER = range(1, 13)


class HolidayKindEnum(Enum):
    FIXED = 'FIXED'
    EASTER = 'EASTER'
    MOVING = 'MOVING'
