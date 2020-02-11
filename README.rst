===========
Workingless
===========

Workingless is a lib for holidays calculations. Currently it supports Colombia
holidays. Mexico coming soon.


Usage
-----

Workingless has two methods for the countries supported, they are:
``get_holidays_from_year`` and ``is_holiday``.

Example usage:

.. code-block:: python

    import datetime

    from workingless import countries

    colombia = countries.COL()
    holidays = colombia.get_holidays_from_year(year=2020)
    print(type(holidays))  # <class 'generator'>
    print(list(holidays))
    # result:
    # [
    #     datetime.date(2020, 1, 1),
    #     datetime.date(2020, 1, 6),
    #     datetime.date(2020, 3, 23),
    #     datetime.date(2020, 4, 5),
    #     datetime.date(2020, 4, 9),
    #     datetime.date(2020, 4, 10),
    #     datetime.date(2020, 4, 12),
    #     datetime.date(2020, 5, 1),
    #     datetime.date(2020, 5, 25),
    #     datetime.date(2020, 6, 15),
    #     datetime.date(2020, 6, 22),
    #     datetime.date(2020, 6, 29),
    #     datetime.date(2020, 7, 20),
    #     datetime.date(2020, 8, 7),
    #     datetime.date(2020, 8, 17),
    #     datetime.date(2020, 10, 12),
    #     datetime.date(2020, 11, 2),
    #     datetime.date(2020, 11, 16),
    #     datetime.date(2020, 12, 8),
    #     datetime.date(2020, 12, 25)
    # ]
    colombia.is_holiday(date=datetime.date(2020, 1, 1))  # True
