import matplotlib.pyplot as plt


def make_plots(benchmarks):
    plots = {}
    for n, results in benchmarks:
        for result in results:
            if result.min() is -1:
                continue
            if not plots.get(result.name()):
                plots[result.name()] = ([], [])
            plots[result.name()][0].append(n)
            plots[result.name()][1].append(result.min())

    return plots.items()


def display_benchmark_plot(benchmarks, title, loglog=False, stylesheet='Solarize_Light2'):
    plot_results(benchmarks, title, loglog, stylesheet)
    plt.show()


def plot_results(benchmarks, title, loglog=False, stylesheet='Solarize_Light2'):
    with plt.style.context(stylesheet):
        for name, values in make_plots(benchmarks):
            if loglog:
                plt.loglog(values[0], values[1], label=name)
            else:
                plt.plot(values[0], values[1], label=name)
        plt.xlabel('n')
        plt.ylabel('min')
        plt.title(title)
        plt.legend()
    return plt
