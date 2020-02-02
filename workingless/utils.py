import datetime

from dateutil.relativedelta import relativedelta

from workingless.constants import MONDAY


def get_next_day(date: datetime.date, next_day: int = MONDAY) -> datetime.date:
    """
    Get next day if date is not equal than date

    Args:
        date (datetime.date): from date
        next_day (int): next day. MONDAY is default

    Returns:
        date: same date if day from ``date`` is equal to next_date,
            date with next_day otherwise.

    """
    if date.weekday() != next_day:
        date = date + relativedelta(weekday=next_day)
    return date
