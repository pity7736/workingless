import datetime

from pytest import mark

from workingless.constants import JANUARY, MONDAY, TUESDAY, FRIDAY, FEBRUARY, DECEMBER
from workingless.calculators import MovingCalculator


base_dates = (
    (2019, JANUARY, 6, MONDAY, datetime.date(2019, JANUARY, 7)),
    (2019, JANUARY, 6, TUESDAY, datetime.date(2019, JANUARY, 8)),
    (2019, JANUARY, 6, FRIDAY, datetime.date(2019, JANUARY, 11)),
    (2020, FEBRUARY, 1, FRIDAY, datetime.date(2020, FEBRUARY, 7)),
    (2020, DECEMBER, 31, FRIDAY, datetime.date(2021, JANUARY, 1)),
)


@mark.parametrize('year, month, day, next_day, expected_date', base_dates)
def test_calculate(year, month, day, next_day, expected_date):
    calculator = MovingCalculator(month=month, day=day, next_day=next_day)

    assert calculator.calculate(year=year) == expected_date
