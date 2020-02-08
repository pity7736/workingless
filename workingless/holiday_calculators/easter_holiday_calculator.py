import datetime

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta

from workingless.holiday_calculator import HolidayCalculator


class EasterHolidayCalculator(HolidayCalculator):
    """
    Holidays calculations based in easter date.
    The holiday could be n days +/- from easter date.
    """

    def calculate(self, year: int) -> datetime.date:
        """
        It returns easter date +/- days passed in constructor.

        Args:
            year (int): year for calculate holiday

        Returns:
            datetime.date: holiday date
        """
        return easter(year) + relativedelta(days=self._holiday.days)
