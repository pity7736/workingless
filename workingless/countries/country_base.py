import datetime
from abc import ABCMeta, abstractmethod
from typing import Union, Generator, Tuple

from workingless.constants import SATURDAY, SUNDAY
from workingless.holiday import Holiday


class CountryBase(metaclass=ABCMeta):

    _instance = None
    _base_holidays = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_next_working_day(self, date: datetime.date) -> datetime.date:
        if self.is_working_day(date) is False:
            return self.get_next_working_day(date + datetime.timedelta(days=1))
        return date

    def is_working_day(self, date: datetime.date, ) -> bool:
        return date.weekday() not in (SATURDAY, SUNDAY) and self.is_holiday(date) is False

    def is_holiday(self, date: Union[datetime.date, datetime.datetime]):
        """
        Validate if a date is a holiday

        Args:
            date (datetime.date, datetime.datetime): date to validate.

        Returns:
            bool: True if the date is holiday, False otherwise.
        """
        if isinstance(date, datetime.datetime):
            date = date.date()
        return date in self.get_holidays_from_year(date.year)

    def get_holidays_from_year(self, year) -> Generator[datetime.date, None, None]:
        """
       Get holidays from a specific year

       Args:
           year (int): year

       Returns:
           Generator: holidays from that year.
       """
        for holiday in self._get_base_holidays():
            yield holiday.calculate(year=year)

    def _get_base_holidays(self) -> Tuple[Holiday]:
        if self._base_holidays is None:
            self._base_holidays = self._get_base_country_holidays()
        return self._base_holidays

    @staticmethod
    @abstractmethod
    def _get_base_country_holidays():
        pass
