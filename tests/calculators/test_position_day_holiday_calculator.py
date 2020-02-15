import datetime

from pytest import mark, raises

from workingless.constants import FEBRUARY, MONDAY, MARCH, JANUARY
from workingless.calculators import PositionDayCalculator


base_dates = (
    (2020, FEBRUARY, 1, 1, MONDAY, datetime.date(2020, FEBRUARY, 3)),
    (2020, FEBRUARY, 1, 3, MONDAY, datetime.date(2020, FEBRUARY, 17)),
    (2020, MARCH, 1, 5, MONDAY, datetime.date(2020, MARCH, 30)),
)


@mark.parametrize('year, month, day, position, weekday, expected_date', base_dates)
def test_calculate(year, month, day, position, weekday, expected_date):
    calculator = PositionDayCalculator(month=month, day=day, position=position, weekday=weekday)

    assert calculator.calculate(year=year) == expected_date


position_params = (
    (2020, FEBRUARY, 1, 6, MONDAY),
    (2020, FEBRUARY, 1, 0, MONDAY),
    (2020, FEBRUARY, 1, 7, MONDAY),
    (2020, FEBRUARY, 1, -1, MONDAY),
)


@mark.parametrize('year, month, day, position, weekday', position_params)
def test_validate_position(year, month, day, position, weekday):
    with raises(ValueError):
        PositionDayCalculator(month=month, day=day, position=position, weekday=weekday)


wrong_base_dates = (
    (2020, JANUARY, 1, 5, MONDAY),
    (2020, FEBRUARY, 1, 5, MONDAY),
)


@mark.parametrize('year, month, day, position, weekday', wrong_base_dates)
def test_wrong_base_dates(year, month, day, position, weekday):
    calculator = PositionDayCalculator(month=month, day=day, position=position, weekday=weekday)

    with raises(ValueError):
        calculator.calculate(year)
