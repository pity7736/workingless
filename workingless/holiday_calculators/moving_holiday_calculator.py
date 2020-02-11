import datetime

from workingless.holiday_calculator import HolidayCalculator
from workingless.utils import get_next_day


class MovingHolidayCalculator(HolidayCalculator):
    """
    Holidays calculation based in moving date if
    date isn't the specific date.
    For example: base date is january 6, if that date is not monday,
    holiday will be next monday.

    """

    def calculate(self, year):
        """
        Calcule holiday from base date

        Args:
            year (int): year for calculate holiday

        Returns:
            datetime.date: holiday date
        """
        return get_next_day(datetime.date(year, self._holiday.month, self._holiday.day))
