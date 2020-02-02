import datetime

from dateutil.relativedelta import relativedelta

from workingless.constants import MONDAY


def get_next_day(date: datetime.date, next_day: int = MONDAY) -> datetime.date:
    if date.weekday() != next_day:
        date = date + relativedelta(weekday=next_day)
    return date
