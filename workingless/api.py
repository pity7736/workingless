import datetime

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta


def get_holidays_from_year(year):
    result = [datetime.date(year, 1, 1)]
    a = datetime.date(year, 1, 6)
    if a.weekday() != 0:
        a = a + relativedelta(weekday=0)
    result.append(a)

    b = datetime.date(year, 3, 19)
    if b.weekday() != 0:
        b = b + relativedelta(weekday=0)
    result.append(b)
    easter_day = easter(year=year)
    c = easter_day - relativedelta(days=7)
    result.append(c)
    result.append(easter_day - relativedelta(days=3))
    result.append(easter_day - relativedelta(days=2))
    result.append(easter_day)
    result.append(datetime.date(year, 5, 1))
    result.append(easter_day + relativedelta(days=43))
    result.append(easter_day + relativedelta(days=64))
    result.append(easter_day + relativedelta(days=71))
    d = datetime.date(year, 6, 29)
    if d.weekday() != 0:
        d = d + relativedelta(weekday=0)
    result.append(d)
    result.append(datetime.date(year, 7, 20))
    result.append(datetime.date(year, 8, 7))
    e = datetime.date(year, 8, 15)
    if e.weekday() != 0:
        e = e + relativedelta(weekday=0)
    result.append(e)
    f = datetime.date(year, 10, 12)
    if f.weekday() != 0:
        f = f + relativedelta(weekday=0)
    result.append(f)
    g = datetime.date(year, 11, 1)
    if g.weekday() != 0:
        g = g + relativedelta(weekday=0)
    result.append(g)
    h = datetime.date(year, 11, 11)
    if h.weekday() != 0:
        h = h + relativedelta(weekday=0)
    result.append(h)
    result.append(datetime.date(year, 12, 8))
    result.append(datetime.date(year, 12, 25))
    return result
