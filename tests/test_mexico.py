import datetime

from pytest import mark


years_holidays = (
    (
        2020,
        (
            datetime.date(2020, 1, 1),
            datetime.date(2020, 2, 3),
            datetime.date(2020, 3, 16),
            datetime.date(2020, 4, 10),
            datetime.date(2020, 5, 1),
            datetime.date(2020, 9, 16),
            datetime.date(2020, 11, 16),
            datetime.date(2020, 12, 25)
        )
    ),
    (
        2018,
        (
            datetime.date(2018, 1, 1),
            datetime.date(2018, 2, 5),
            datetime.date(2018, 3, 19),
            datetime.date(2018, 3, 30),
            datetime.date(2018, 5, 1),
            datetime.date(2018, 9, 16),
            datetime.date(2018, 11, 19),
            datetime.date(2018, 12, 1),
            datetime.date(2018, 12, 25)
        )
    ),
    (
        2016,
        (
            datetime.date(2016, 1, 1),
            datetime.date(2016, 2, 1),
            datetime.date(2016, 3, 21),
            datetime.date(2016, 3, 25),
            datetime.date(2016, 5, 1),
            datetime.date(2016, 9, 16),
            datetime.date(2016, 11, 21),
            datetime.date(2016, 12, 25)
        )
    ),
    (
        2021,
        (
            datetime.date(2021, 1, 1),
            datetime.date(2021, 2, 1),
            datetime.date(2021, 3, 15),
            datetime.date(2021, 4, 2),
            datetime.date(2021, 5, 1),
            datetime.date(2021, 9, 16),
            datetime.date(2021, 11, 15),
            datetime.date(2021, 12, 25)
        )
    ),
    (
        2023,
        (
            datetime.date(2023, 1, 1),
            datetime.date(2023, 2, 6),
            datetime.date(2023, 3, 20),
            datetime.date(2023, 4, 7),
            datetime.date(2023, 5, 1),
            datetime.date(2023, 9, 16),
            datetime.date(2023, 11, 20),
            datetime.date(2023, 12, 25)
        )
    ),
    (
        2024,
        (
            datetime.date(2024, 1, 1),
            datetime.date(2024, 2, 5),
            datetime.date(2024, 3, 18),
            datetime.date(2024, 3, 29),
            datetime.date(2024, 5, 1),
            datetime.date(2024, 9, 16),
            datetime.date(2024, 11, 18),
            datetime.date(2024, 12, 1),
            datetime.date(2024, 12, 25)
        )
    ),
)


@mark.parametrize('year, expected_holidays', years_holidays)
def test_get_holidays_from_year(year, expected_holidays, mex_fixture):
    holidays = mex_fixture.get_holidays_from_year(year=year)

    assert tuple(holidays) == expected_holidays


dates = (
    (datetime.date(2001, 1, 1), True),
    (datetime.date(2001, 4, 13), True),
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
