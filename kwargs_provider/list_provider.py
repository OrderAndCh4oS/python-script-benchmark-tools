from kwargs_provider.kwargs_provider import KwargsProvider


class ListProvider(KwargsProvider):

    def __init__(self, n):
        self.arr = list(range(n))

    def get(self):
        return {'arr': self.arr}
