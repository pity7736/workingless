import datetime

from pytest import mark

from workingless.constants import JANUARY, MAY, NOVEMBER
from workingless.holiday_calculators import FixedHolidayCalculator


base_dates = (
    (2020, JANUARY, 1),
    (2020, MAY, 1),
    (1990, NOVEMBER, 25)
)


@mark.parametrize('year, month, day', base_dates)
def test_calculator(year, month, day):
    calculator = FixedHolidayCalculator(month=month, day=day)

    assert calculator.calculate(year=year) == datetime.date(year, month, day)
