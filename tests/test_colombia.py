import datetime

from pytest import mark


years_holidays = (
    (
        2020,
        [
            datetime.date(2020, 1, 1),
            datetime.date(2020, 1, 6),
            datetime.date(2020, 3, 23),
            datetime.date(2020, 4, 5),
            datetime.date(2020, 4, 9),
            datetime.date(2020, 4, 10),
            datetime.date(2020, 4, 12),
            datetime.date(2020, 5, 1),
            datetime.date(2020, 5, 25),
            datetime.date(2020, 6, 15),
            datetime.date(2020, 6, 22),
            datetime.date(2020, 6, 29),
            datetime.date(2020, 7, 20),
            datetime.date(2020, 8, 7),
            datetime.date(2020, 8, 17),
            datetime.date(2020, 10, 12),
            datetime.date(2020, 11, 2),
            datetime.date(2020, 11, 16),
            datetime.date(2020, 12, 8),
            datetime.date(2020, 12, 25)
        ]
    ),
    (
        2015,
        [
            datetime.date(2015, 1, 1),
            datetime.date(2015, 1, 12),
            datetime.date(2015, 3, 23),
            datetime.date(2015, 3, 29),
            datetime.date(2015, 4, 2),
            datetime.date(2015, 4, 3),
            datetime.date(2015, 4, 5),
            datetime.date(2015, 5, 1),
            datetime.date(2015, 5, 18),
            datetime.date(2015, 6, 8),
            datetime.date(2015, 6, 15),
            datetime.date(2015, 6, 29),
            datetime.date(2015, 7, 20),
            datetime.date(2015, 8, 7),
            datetime.date(2015, 8, 17),
            datetime.date(2015, 10, 12),
            datetime.date(2015, 11, 2),
            datetime.date(2015, 11, 16),
            datetime.date(2015, 12, 8),
            datetime.date(2015, 12, 25)
        ]
    ),
    (
        2000,
        [
            datetime.date(2000, 1, 1),
            datetime.date(2000, 1, 10),
            datetime.date(2000, 3, 20),
            datetime.date(2000, 4, 16),
            datetime.date(2000, 4, 20),
            datetime.date(2000, 4, 21),
            datetime.date(2000, 4, 23),
            datetime.date(2000, 5, 1),
            datetime.date(2000, 6, 5),
            datetime.date(2000, 6, 26),
            datetime.date(2000, 7, 3),
            datetime.date(2000, 7, 3),
            datetime.date(2000, 7, 20),
            datetime.date(2000, 8, 7),
            datetime.date(2000, 8, 21),
            datetime.date(2000, 10, 16),
            datetime.date(2000, 11, 6),
            datetime.date(2000, 11, 13),
            datetime.date(2000, 12, 8),
            datetime.date(2000, 12, 25)
        ]
    ),
    (
        2023,
        [
            datetime.date(2023, 1, 1),
            datetime.date(2023, 1, 9),
            datetime.date(2023, 3, 20),
            datetime.date(2023, 4, 2),
            datetime.date(2023, 4, 6),
            datetime.date(2023, 4, 7),
            datetime.date(2023, 4, 9),
            datetime.date(2023, 5, 1),
            datetime.date(2023, 5, 22),
            datetime.date(2023, 6, 12),
            datetime.date(2023, 6, 19),
            datetime.date(2023, 7, 3),
            datetime.date(2023, 7, 20),
            datetime.date(2023, 8, 7),
            datetime.date(2023, 8, 21),
            datetime.date(2023, 10, 16),
            datetime.date(2023, 11, 6),
            datetime.date(2023, 11, 13),
            datetime.date(2023, 12, 8),
            datetime.date(2023, 12, 25)
        ]
    ),
    (
        1999,
        [
            datetime.date(1999, 1, 1),
            datetime.date(1999, 1, 11),
            datetime.date(1999, 3, 22),
            datetime.date(1999, 3, 28),
            datetime.date(1999, 4, 1),
            datetime.date(1999, 4, 2),
            datetime.date(1999, 4, 4),
            datetime.date(1999, 5, 1),
            datetime.date(1999, 5, 17),
            datetime.date(1999, 6, 7),
            datetime.date(1999, 6, 14),
            datetime.date(1999, 7, 5),
            datetime.date(1999, 7, 20),
            datetime.date(1999, 8, 7),
            datetime.date(1999, 8, 16),
            datetime.date(1999, 10, 18),
            datetime.date(1999, 11, 1),
            datetime.date(1999, 11, 15),
            datetime.date(1999, 12, 8),
            datetime.date(1999, 12, 25)
        ]
    )
)


@mark.parametrize('year, expected_holidays', years_holidays)
def test_get_holidays_from_year(year, expected_holidays, col_fixture):
    holidays = col_fixture.get_holidays_from_year(year=year)

    assert list(holidays) == expected_holidays


dates = (
    (datetime.date(2001, 4, 13), True),
    (datetime.date(2001, 5, 28), True),
    (datetime.date(2001, 6, 18), True),
    (datetime.date(2001, 12, 31), False),
    (datetime.date(2001, 12, 31), False),
    (datetime.date(2001, 12, 31), False),
    (datetime.date(2020, 2, 29), False),
    (datetime.date(2022, 5, 30), True),
    (datetime.date(2022, 7, 3), False),
    (datetime.date(2022, 7, 4), True),
    (datetime.datetime(2022, 7, 4), True),
    (datetime.datetime(2022, 7, 5), False),
)


@mark.parametrize('date, result', dates)
def test_is_holiday(date, result, col_fixture):
    assert col_fixture.is_holiday(date=date) is result


working_days = (
    (datetime.date(2020, 2, 10), True),
    (datetime.date(2020, 2, 11), True),
    (datetime.date(2020, 2, 14), True),
    (datetime.date(2020, 2, 15), False),
    (datetime.date(2020, 2, 16), False),
    (datetime.date(2020, 2, 16), False),
    (datetime.date(2020, 5, 1), False),
)


@mark.parametrize('date, expected_result', working_days)
def test_is_working_day(date, expected_result, col_fixture):
    assert col_fixture.is_working_day(date=date) is expected_result


next_workking_days = (
    (datetime.date(2020, 2, 10), datetime.date(2020, 2, 10)),
    (datetime.date(2020, 2, 14), datetime.date(2020, 2, 14)),
    (datetime.date(2020, 2, 15), datetime.date(2020, 2, 17)),
    (datetime.date(2020, 5, 1), datetime.date(2020, 5, 4)),
)


@mark.parametrize('date, expected_result', next_workking_days)
def test_get_next_working_day(date, expected_result, col_fixture):
    result = col_fixture.get_next_working_day(date=date)
    assert result == expected_result
