from itertools import groupby
from operator import itemgetter

from charts.plot_visual import display_benchmark_plot
from kwargs_provider.dict_t_v_o_values import DictTVOValuesProvider
from run_benchmarks import run_benchmarks
from script import Script


def sarcoma(arr):
    lookup = {}
    result = []
    for row in arr:
        t, v = row['T'], row['V']
        if not lookup.get(t):
            lookup[t] = (v, len(result))
            result.append(row)
            continue

        lt = lookup[t]
        lv, li = lt[0], lt[1]
        if v > lv:
            lookup[t] = (v, li)
            result[li] = row

    return result


def DeepSpace(arr):
    arr.sort(key=lambda val: val['T'])
    return [max(group, key=lambda d: d['V']) for _, group in groupby(arr, key=lambda d: d['T'])]


def RoadRunner(arr):
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


def Patrick_Artner(arr):
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


def run_scripts_with_n_sized_list(scripts, n):
    arr_provider = DictTVOValuesProvider(n)
    return n, run_benchmarks(scripts, arr_provider, 100)


if __name__ == '__main__':
    scripts = (
        Script(sarcoma, 'sarcoma'),
        Script(DeepSpace, 'DeepSpace'),
        Script(RoadRunner, 'RoadRunner'),
        Script(Patrick_Artner, 'Patrick_Artner')
    )

    start = 0
    stop = 25000
    step = 2500

    list_benchmarks = map(lambda n: run_scripts_with_n_sized_list(scripts, n), range(start, stop, step))

    display_benchmark_plot(list_benchmarks, 'Benchmarks')

    arr = [
        {'T': 2345, 'V': 50, 'O': 5},
        {'T': 1234, 'V': 10, 'O': 1},
        {'T': 1234, 'V': 20, 'O': 1},
        {'T': 1234, 'V': 10, 'O': 1},
        {'T': 2345, 'V': 30, 'O': 3},
        {'T': 2345, 'V': 30, 'O': 3},
        {'T': 2345, 'V': 100, 'O': 3},
        {'T': 2345, 'V': 30, 'O': 3},
        {'T': 2345, 'V': 30, 'O': 3},
        {'T': 3456, 'V': 40, 'O': 91}
    ]
