from itertools import groupby
from operator import itemgetter

from examples.provider.dict_t_v_o_values import DictTVOValuesProvider
from examples.provider.dict_t_v_o_values_sorted import DictTVOValuesSortedProvider
from script_benchmark_tools.benchmark_results import display_benchmark_results
from script_benchmark_tools.charts.plot_visual import display_benchmark_plot
from script_benchmark_tools.execute_benchmarks import execute_benchmarks
from script_benchmark_tools.script import Script


def sarcoma(arr):
    lookup = {}
    result = []
    for row in arr:
        row_key, row_value = row['T'], row['V']
        if not lookup.get(row_key):
            lookup[row_key] = (row_value, len(result))
            result.append(row)
            continue

        lookup_value, result_index = lookup[row_key][0], lookup[row_key][1]
        if row_value > lookup_value:
            lookup[row_key] = (row_value, result_index)
            result[result_index] = row

    return result


def deep_space_with_sort(arr):
    arr.sort(key=lambda val: val['T'])
    return [max(group, key=lambda d: d['V']) for _, group in groupby(arr, key=lambda d: d['T'])]


def road_runner_with_sort(arr):
    unique = {}
    arr = sorted(arr, key=itemgetter('T'))
    for dic in arr:
        key = dic['T']
        found = unique.get(key)

        # If value found and doesn't exceed current maximum, just ignore
        if found and dic['V'] <= found['V']:
            continue

        # otherwise just update normally
        unique[key] = dic

    return list(unique.values())


def patrick_artner_with_sort(arr):
    arr = sorted(arr, key=lambda x: x["T"])
    arr2 = []
    for e in arr:
        t, v, o = e["T"], e["V"], e["O"]

        if arr2 and arr2[-1]["T"] == t:
            if arr2[-1]["V"] < v:
                arr2[-1]["V"] = v
                arr2[-1]["O"] = o
        else:
            arr2.append(e)

    return arr2


def deep_space(arr):
    return [max(group, key=lambda d: d['V']) for _, group in groupby(arr, key=lambda d: d['T'])]


def road_runner(arr):
    unique = {}
    for dic in arr:
        key = dic['T']
        found = unique.get(key)

        # If value found and doesn't exceed current maximum, just ignore
        if found and dic['V'] <= found['V']:
            continue

        # otherwise just update normally
        unique[key] = dic

    return list(unique.values())


def road_runner_without_conversion(arr):
    unique = {}
    for dic in arr:
        key = dic['T']
        found = unique.get(key)

        # If value found and doesn't exceed current maximum, just ignore
        if found and dic['V'] <= found['V']:
            continue

        # otherwise just update normally
        unique[key] = dic

    return unique


def patrick_artner(arr):
    arr2 = []
    for e in arr:
        t, v, o = e["T"], e["V"], e["O"]

        if arr2 and arr2[-1]["T"] == t:
            if arr2[-1]["V"] < v:
                arr2[-1]["V"] = v
                arr2[-1]["O"] = o
        else:
            arr2.append(e)

    return arr2


def run_scripts_with_n_sized_sorted_list(scripts, n):
    arr_provider = DictTVOValuesSortedProvider(n)
    return n, execute_benchmarks(scripts, arr_provider, 100)


def run_scripts_with_n_sized_unsorted_list(scripts, n):
    arr_provider = DictTVOValuesProvider(n)
    return n, execute_benchmarks(scripts, arr_provider, 100)


if __name__ == '__main__':

    all_scripts = (
        Script(sarcoma, 'sarcoma'),
        Script(deep_space, 'DeepSpace'),
        Script(road_runner, 'RoadRunner'),
        Script(patrick_artner, 'Patrick_Artner'),
        Script(road_runner_without_conversion, 'RoadRunner'),
        Script(deep_space_with_sort, 'DeepSpace'),
        Script(road_runner_with_sort, 'RoadRunner'),
        Script(patrick_artner_with_sort, 'Patrick_Artner')
    )

    print('Proofs\n------')

    for script in all_scripts:
        print(script.name())
        print(script(arr=[
            {'T': 1234, 'V': 10, 'O': 1},
            {'T': 2345, 'V': 50, 'O': 5},
            {'T': 2345, 'V': 30, 'O': 3},
            {'T': 3456, 'V': 40, 'O': 91}
        ]))

    sort_scripts = (
        Script(sarcoma, 'sarcoma'),
        Script(deep_space, 'DeepSpace'),
        Script(road_runner, 'RoadRunner'),
        Script(patrick_artner, 'Patrick_Artner'),
    )

    title = 'Sorted Benchmarks'

    list_benchmarks = map(lambda n: run_scripts_with_n_sized_sorted_list(sort_scripts, n), [10, 100, 1000, 10000, 25000])
    results = [(n, result) for n, result in list_benchmarks]

    display_benchmark_plot(results, title)

    print(title)
    for n, result in results:
        print('N = %d\n------' % n)
        display_benchmark_results(result)

    unsorted_scripts = (
        Script(sarcoma, 'sarcoma'),
        Script(deep_space_with_sort, 'DeepSpace'),
        Script(road_runner_with_sort, 'RoadRunner'),
        Script(patrick_artner_with_sort, 'Patrick_Artner'),
    )

    title = 'Unsorted Benchmarks'

    list_benchmarks = map(lambda n: run_scripts_with_n_sized_unsorted_list(unsorted_scripts, n), [10, 100, 1000, 10000, 25000])
    results = [(n, result) for n, result in list_benchmarks]

    display_benchmark_plot(results, title)

    print(title)
    for n, result in results:
        print('N = %d\n------' % n)
        display_benchmark_results(result)
