from abc import ABCMeta, abstractmethod


class KwargsProvider(metaclass=ABCMeta):

    @abstractmethod
    def get(self):
        pass
