from script_benchmark_tools import ListProvider, execute_benchmarks


def run_scripts_with_n_sized_list(scripts, n):
    arr_provider = ListProvider(n)
    return n, execute_benchmarks(scripts, arr_provider, 100)
