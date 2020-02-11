import datetime

from pytest import mark

from workingless import countries


years_holidays = (
    (
        2020,
        # just fixed for now
        [
            datetime.date(2020, 1, 1),
            datetime.date(2020, 5, 1),
            datetime.date(2020, 9, 16),
            datetime.date(2020, 12, 25)
        ]
    ),
)


@mark.parametrize('year, expected_holidays', years_holidays)
def test_get_holidays_from_year(year, expected_holidays, mex_fixture):
    holidays = mex_fixture.get_holidays_from_year(year=year)

    assert list(holidays) == expected_holidays


dates = (
    (datetime.date(2001, 1, 1), True),
    (datetime.date(2001, 4, 13), False),
    (datetime.date(2001, 5, 28), False),
    (datetime.date(2001, 6, 18), False),
    (datetime.date(2001, 9, 16), True),
    (datetime.date(2001, 12, 31), False),
    (datetime.date(2001, 12, 31), False),
    (datetime.date(2001, 12, 25), True),
    (datetime.date(2001, 12, 31), False),
    (datetime.date(2020, 2, 29), False),
    (datetime.date(2022, 5, 30), False),
    (datetime.date(2022, 7, 3), False),
    (datetime.date(2022, 7, 4), False),
    (datetime.datetime(2022, 7, 4), False),
    (datetime.datetime(2022, 7, 5), False),
)


@mark.parametrize('date, result', dates)
def test_is_holiday(date, result, mex_fixture):
    assert mex_fixture.is_holiday(date=date) is result
