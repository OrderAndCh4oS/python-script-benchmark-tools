from script_benchmark_tools import KwargsProvider


class RangeProvider(KwargsProvider):

    def __init__(self, n):
        self.arr = range(n)

    def get(self):
        return {'arr': self.arr}
