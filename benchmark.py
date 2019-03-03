from result import Result
from timer import timer


def benchmark(script, kwargs, n_runs=1000):
    run_times = []
    for _ in range(n_runs):
        time = timer(script, kwargs)
        run_times.append(time)

    return Result(script, run_times, n_runs)
