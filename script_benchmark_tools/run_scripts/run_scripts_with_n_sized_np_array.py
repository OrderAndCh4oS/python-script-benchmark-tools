from script_benchmark_tools import NpArrayProvider, execute_benchmarks


def run_scripts_with_n_sized_np_array(scripts, n):
    arr_provider = NpArrayProvider(n)
    return n, execute_benchmarks(scripts, arr_provider, 100)
