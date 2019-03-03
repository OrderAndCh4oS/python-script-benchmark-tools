import numpy as np

from display_benchmark_results import display_benchmark_results
from kwargs_provider.list_provider import ListProvider
from kwargs_provider.np_arange_provider import NpARangeProvider
from kwargs_provider.np_array_provider import NpArrayProvider
from kwargs_provider.range_provider import RangeProvider
from plot import plot
from run_benchmarks import run_benchmarks
from script import Script


def reversed_loop(arr):
    r = []
    last = 0
    a = arr[::-1]
    for x in a:
        r.append(x + last)
        last += x
    return r[::-1]


def sum_first(arr):
    t = sum(arr)
    r = []
    for a in arr:
        r.append(t)
        t -= a
    return r


class Generator:
    __name__ = 'generator'

    def __call__(self, arr):
        return [*self.generate(arr[::-1])][::-1]

    def generate(self, a):
        r = 0
        for x in a:
            r += x
            yield r


def reverse_sum(arr):
    if not isinstance(arr, list):
        return False
    last = 0
    r = []
    for i in reversed(range(0, len(arr))):
        last = arr[i] + last
        r.append(last)
    return r[::-1]


def run_scripts_with_n_sized_list(scripts, n):
    arr_provider = ListProvider(n)
    return n, run_benchmarks(scripts, arr_provider, 1000)


def run_scripts_with_n_sized_range(scripts, n):
    arr_provider = RangeProvider(n)
    return n, run_benchmarks(scripts, arr_provider, 1000)


def run_scripts_with_n_sized_np_arange(scripts, n):
    arr_provider = NpARangeProvider(n)
    return n, run_benchmarks(scripts, arr_provider, 1000)


def run_scripts_with_n_sized_np_array(scripts, n):
    arr_provider = NpArrayProvider(n)
    return n, run_benchmarks(scripts, arr_provider, 1000)


if __name__ == '__main__':
    scripts = (
        Script(reversed_loop, 'sarcoma'),
        Script(sum_first, 'sarcoma'),
        Script(Generator(), 'sarcoma'),
        Script(reverse_sum, 'sarcoma')
    )

    list_benchmarks = map(lambda n: run_scripts_with_n_sized_list(scripts, n), range(100, 1000, 100))
    range_benchmarks = map(lambda n: run_scripts_with_n_sized_range(scripts, n), range(100, 1000, 100))
    np_arange_benchmarks = map(lambda n: run_scripts_with_n_sized_np_arange(scripts, n), range(100, 10000, 100))
    np_array_benchmarks = map(lambda n: run_scripts_with_n_sized_np_array(scripts, n), range(100, 10000, 100))

    import matplotlib.pyplot as plt

    def make_plots(benchmarks):
        plots = {}
        for n, results in benchmarks:
            for result in results:
                if not plots.get(result.name()):
                    plots[result.name()] = ([], [])
                plots[result.name()][0].append(n)
                plots[result.name()][1].append(result.average())

        return plots


    list_plots = make_plots(list_benchmarks)
    range_plots = make_plots(range_benchmarks)

    for name, values in list_plots.items():
        plt.plot(values[0], values[1], label='List %s' % name)


    for name, values in range_plots.items():
        plt.plot(values[0], values[1], label='Range %s' % name)

    plt.xlabel('n')
    plt.ylabel('average')

    plt.title("Benchmarks")
    plt.legend()
    plt.show()

    #
    # for p in plots:
    #     plot(plots[p], 1000, 0.00025)

    # print('List')
    #
    # for _, results in list_benchmarks:
    #     display_benchmark_results(results)
    #
    # print('Range')
    #
    # for _, results in range_benchmarks:
    #     display_benchmark_results(results)
    #
    # print('Np Arange')
    #
    # for _, results in np_arange_benchmarks:
    #     display_benchmark_results(results)
    #
    # print('Np Array')
    #
    # for _, results in np_array_benchmarks:
    #     display_benchmark_results(results)
