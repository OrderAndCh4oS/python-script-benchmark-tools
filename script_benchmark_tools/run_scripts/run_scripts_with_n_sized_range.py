from script_benchmark_tools import RangeProvider, execute_benchmarks


def run_scripts_with_n_sized_range(scripts, n):
    arr_provider = RangeProvider(n)
    return n, execute_benchmarks(scripts, arr_provider, 100)
