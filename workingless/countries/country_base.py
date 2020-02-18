import datetime
from abc import ABCMeta, abstractmethod
from typing import Union, Generator

from workingless.constants import SATURDAY, SUNDAY


class CountryBase(metaclass=ABCMeta):

    __slots__ = ()
    _instance = None
    _base_holidays = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_next_working_day(self, date: datetime.date) -> datetime.date:
        """
        Get next working day from date.

        Args:
            date (datetime.date): from date

        Returns:
            datetime.date: next working day

        """
        if self.is_working_day(date) is False:
            return self.get_next_working_day(date + datetime.timedelta(days=1))
        return date

    def is_working_day(self, date: datetime.date, ) -> bool:
        """
        Evaluate if date is a working day.

        Args:
            date (datetime.date): date to evaluate

        Returns:
            bool: True is date is a working day, False otherwise.

        """
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
            holiday_date = holiday.calculate(year=year)
            if holiday_date:
                yield holiday_date

    def _get_base_holidays(self):
        if self._base_holidays is None:
            self.__class__._base_holidays = self._get_base_country_holidays()
        return self._base_holidays

    @staticmethod
    @abstractmethod
    def _get_base_country_holidays():
        pass
