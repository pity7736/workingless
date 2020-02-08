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
    # [
    #     datetime.date(2020, 1, 1),
    #     datetime.date(2020, 1, 6),
    #     datetime.date(2020, 3, 23),
    #     datetime.date(2020, 4, 5),
    #     datetime.date(2020, 4, 9),
    #     datetime.date(2020, 4, 10),
    #     datetime.date(2020, 4, 12),
    #     datetime.date(2020, 5, 1),
    #     datetime.date(2020, 5, 25),
    #     datetime.date(2020, 6, 15),
    #     datetime.date(2020, 6, 22),
    #     datetime.date(2020, 6, 29),
    #     datetime.date(2020, 7, 20),
    #     datetime.date(2020, 8, 7),
    #     datetime.date(2020, 8, 17),
    #     datetime.date(2020, 10, 12),
    #     datetime.date(2020, 11, 2),
    #     datetime.date(2020, 11, 16),
    #     datetime.date(2020, 12, 8),
    #     datetime.date(2020, 12, 25)
    # ]
