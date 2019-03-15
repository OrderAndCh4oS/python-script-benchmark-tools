from copy import deepcopy

from script_benchmark_tools.result import Result
from script_benchmark_tools.timer import timer


def benchmark(script, kwargs, n_runs=1000):
    run_times = []
    for _ in range(n_runs):
        time = timer(script, deepcopy(kwargs))
        run_times.append(time)

    return Result(script, run_times, n_runs)

