
import matplotlib.pyplot as plt
import numpy as np

from charts.plot_visual import display_benchmark_plot
from kwargs_provider.list_provider import ListProvider
from kwargs_provider.np_arange_provider import NpARangeProvider
from kwargs_provider.np_array_provider import NpArrayProvider
from kwargs_provider.range_provider import RangeProvider
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


def josep_joestar(arr):
    if not isinstance(arr, list):
        return False
    for i in range(len(arr) - 2, -1, -1):
        arr[i] += arr[i + 1]
    return arr


def alain_t(arr):
    return np.sum(np.triu(arr), 1)


def user2699(arr):
    return np.add.accumulate(arr[::-1])[::-1]


def stuart(arr):
    return np.flip(np.cumsum(np.flip(arr)))


def stuart_two(arr):
    return np.cumsum(arr[::-1])[::-1]


def student(arr):
    return [sum(arr[i:]) for i in range(len(arr))]


def run_scripts_with_n_sized_list(scripts, n):
    arr_provider = ListProvider(n)
    return n, run_benchmarks(scripts, arr_provider, 100)


def run_scripts_with_n_sized_range(scripts, n):
    arr_provider = RangeProvider(n)
    return n, run_benchmarks(scripts, arr_provider, 100)


def run_scripts_with_n_sized_np_arange(scripts, n):
    arr_provider = NpARangeProvider(n)
    return n, run_benchmarks(scripts, arr_provider, 100)


def run_scripts_with_n_sized_np_array(scripts, n):
    arr_provider = NpArrayProvider(n)
    return n, run_benchmarks(scripts, arr_provider, 100)


if __name__ == '__main__':
    scripts = (
        Script(reversed_loop, 'sarcoma'),
        Script(sum_first, 'sarcoma'),
        Script(Generator(), 'sarcoma'),
        Script(reverse_sum, 'sarcoma'),
        Script(josep_joestar, 'josep_joestar'),
        Script(alain_t, 'alain_t'),
        Script(user2699, 'user2699'),
        Script(stuart, 'stuart'),
        Script(stuart_two, 'stuart2'),
        Script(student, 'student'),
    )

    start = 10
    stop = 100
    step = 10

    list_benchmarks = map(lambda n: run_scripts_with_n_sized_list(scripts, n), range(start, stop, step))
    range_benchmarks = map(lambda n: run_scripts_with_n_sized_range(scripts, n), range(start, stop, step))
    np_arange_benchmarks = map(lambda n: run_scripts_with_n_sized_np_arange(scripts, n), range(start, stop, step))
    np_array_benchmarks = map(lambda n: run_scripts_with_n_sized_np_array(scripts, n), range(start, stop, step))

    display_benchmark_plot(list_benchmarks, 'List Benchmarks')
    display_benchmark_plot(range_benchmarks, 'Range Benchmarks')
    display_benchmark_plot(np_array_benchmarks, 'NP Array Benchmarks')
    display_benchmark_plot(np_arange_benchmarks, 'NP ARange Benchmarks')

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
