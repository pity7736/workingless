import datetime

from dateutil.relativedelta import relativedelta

from workingless.holiday_calculator import HolidayCalculator


class NDayHolidayCalculator(HolidayCalculator):

    def calculate(self, year: int) -> datetime.date:
        base_date = datetime.date(year=year, month=self._holiday.month, day=self._holiday.day)
        first_date = base_date + relativedelta(weekday=self._holiday.weekday)
        return first_date + relativedelta(days=7 * (self._holiday.n_day - 1))
