import numpy as np

from script_benchmark_tools.benchmark_results import display_benchmark_results
from script_benchmark_tools.charts.plot_visual import display_benchmark_plot
from script_benchmark_tools.run_scripts.run_scripts_with_n_sized_list import run_scripts_with_n_sized_list
from script_benchmark_tools.run_scripts.run_scripts_with_n_sized_np_arange import run_scripts_with_n_sized_np_arange
from script_benchmark_tools.run_scripts.run_scripts_with_n_sized_np_array import run_scripts_with_n_sized_np_array
from script_benchmark_tools.run_scripts.run_scripts_with_n_sized_range import run_scripts_with_n_sized_range
from script_benchmark_tools.script import Script


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


if __name__ == '__main__':
    scripts = (
        Script(reversed_loop, 'sarcoma'),
        Script(sum_first, 'sarcoma'),
        Script(Generator(), 'sarcoma'),
        Script(reverse_sum, 'sarcoma'),
        Script(josep_joestar, 'josep_joestar'),
        # Script(alain_t, 'alain_t'),
        Script(user2699, 'user2699'),
        Script(stuart, 'stuart'),
        Script(stuart_two, 'stuart2'),
        # Script(student, 'student'),
    )

    n_steps = [10, 100, 1000, 5000, 10000]

    list_benchmarks = map(lambda n: run_scripts_with_n_sized_list(scripts, n), n_steps)
    range_benchmarks = map(lambda n: run_scripts_with_n_sized_range(scripts, n), n_steps)
    np_arange_benchmarks = map(lambda n: run_scripts_with_n_sized_np_arange(scripts, n), n_steps)
    np_array_benchmarks = map(lambda n: run_scripts_with_n_sized_np_array(scripts, n), n_steps)

    list_results = [(n, result) for n, result in list_benchmarks]
    range_results = [(n, result) for n, result in range_benchmarks]
    np_array_results = [(n, result) for n, result in np_array_benchmarks]
    np_arange_results = [(n, result) for n, result in np_arange_benchmarks]

    display_benchmark_plot(list_results, 'List Benchmarks')
    display_benchmark_plot(range_results, 'Range Benchmarks')
    display_benchmark_plot(np_array_results, 'NP Array Benchmarks')
    display_benchmark_plot(np_arange_results, 'NP ARange Benchmarks')

    #
    # for p in plots:
    #     plot(plots[p], 1000, 0.00025)

    print('List')

    for _, results in list_results:
        display_benchmark_results(results)

    print('Range')

    for _, results in range_results:
        display_benchmark_results(results)

    print('Np Arange')

    for _, results in np_arange_results:
        display_benchmark_results(results)

    print('Np Array')

    for _, results in np_array_results:
        display_benchmark_results(results)
