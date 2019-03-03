import numpy as np

from kwargs_provider.kwargs_provider import KwargsProvider


class NpARangeProvider(KwargsProvider):

    def __init__(self, n):
        self.arr = np.arange(n)

    def get(self):
        return {'arr': self.arr}
