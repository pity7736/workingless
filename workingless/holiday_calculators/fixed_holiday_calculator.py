import datetime

from workingless.holiday_calculator import HolidayCalculator


class FixedHolidayCalculator(HolidayCalculator):
    """
    This is the simpliest implementation.
    It returns exactly the same date.
    """

    def calculate(self, year: int) -> datetime.date:
        """
        It returns exactly the same date given.

        Args:
            year (int): year for calculate holiday

        Returns:
            datetime.date: holiday date
        """
        return datetime.date(year, self._holiday.month, self._holiday.day)
