import datetime
from abc import abstractmethod, ABCMeta


class HolidayCalculator(metaclass=ABCMeta):
    """
    Base class for holiday calculations.
    If there is another way to calculate holidays, inherit this class,
    override ``calculate`` method and implement it.

    Args:
        holiday (Holiday): ``Holiday`` instance
    """

    __slots__ = ('_holiday',)

    def __init__(self, holiday):
        self._holiday = holiday

    @abstractmethod
    def calculate(self, year: int) -> datetime.date:
        """
        Abstract method to calculate holiday for specific year.

        Args:
            year (int): year for calculate holiday

        Returns:
            datetime.date: holiday date.
        """
