import numpy as np

from kwargs_provider.kwargs_provider import KwargsProvider


class NpArrayProvider(KwargsProvider):

    def __init__(self, n):
        self.arr = np.array(range(n))

    def get(self):
        return {'arr': self.arr}
