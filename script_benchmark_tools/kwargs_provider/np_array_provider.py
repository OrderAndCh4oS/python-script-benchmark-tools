import numpy as np

from script_benchmark_tools import KwargsProvider


class NpArrayProvider(KwargsProvider):

    def __init__(self, n):
        self.arr = np.array(range(n))

    def get(self):
        return {'arr': self.arr}
