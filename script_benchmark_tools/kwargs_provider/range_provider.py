from script_benchmark_tools.kwargs_provider import KwargsProvider


class RangeProvider(KwargsProvider):

    def __init__(self, n):
        self.arr = range(n)

    def get(self):
        return {'arr': self.arr}
