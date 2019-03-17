from script_benchmark_tools import NpARangeProvider, execute_benchmarks


def run_scripts_with_n_sized_np_arange(scripts, n):
    arr_provider = NpARangeProvider(n)
    return n, execute_benchmarks(scripts, arr_provider, 100)
