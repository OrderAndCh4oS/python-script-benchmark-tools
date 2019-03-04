import matplotlib.pyplot as plt


def make_plots(benchmarks):
    plots = {}
    for n, results in benchmarks:
        for result in results:
            if not plots.get(result.name()):
                plots[result.name()] = ([], [])
            plots[result.name()][0].append(n)
            plots[result.name()][1].append(result.average())

    return plots.items()


def display_benchmark_plot(benchmarks, title):
    for name, values in make_plots(benchmarks):
        plt.plot(values[0], values[1], label=name)
    plt.xlabel('n')
    plt.ylabel('average')
    plt.title(title)
    plt.legend()
    plt.show()
