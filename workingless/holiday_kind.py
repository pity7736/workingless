from abc import abstractmethod, ABCMeta


class HolidayKind(metaclass=ABCMeta):

    __slots__ = ('_holiday',)

    def __init__(self, holiday):
        self._holiday = holiday
        pass

    def get_kind(self):
        pass

    @abstractmethod
    def calculate(self, year):
        pass
