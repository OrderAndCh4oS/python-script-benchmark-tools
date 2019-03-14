from random import randint

from script_benchmark_tools.kwargs_provider.kwargs_provider import KwargsProvider


class DictTVOValuesSortedProvider(KwargsProvider):

    def __init__(self, n):
        self.arr = list(self.gen_arr(n))
        self.arr.sort(key=lambda val: val['T'])

    def gen_arr(self, n):
        for _ in range(n):
            yield {'T': randint(1000, 9999), 'V': randint(0, 100), 'O': randint(0, 100)}

    def get(self):
        return {'arr': self.arr}
