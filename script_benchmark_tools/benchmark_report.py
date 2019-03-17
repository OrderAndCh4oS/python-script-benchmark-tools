import os
from copy import copy

from terminal_table import Table

from script_benchmark_tools.benchmark_results import benchmark_results
from script_benchmark_tools.charts.plot_visual import plot_results


def benchmark_report(
        title,
        proof_data,
        filename,
        n_steps,
        benchmark,
        scripts
):
    output, plot = generate_benchmark_report(
        title,
        proof_data,
        filename,
        scripts,
        n_steps,
        benchmark,
    )
    save_benchmark_results(output, filename)
    save_plot(plot, filename)


def generate_benchmark_report(
        title,
        proof_data,
        filename,
        scripts,
        n_steps,
        benchmark,
        use_ansi=False
):
    proof_copy = copy(proof_data)
    output = "#%s\n\n" % title
    output += 'Proofs\n------\n\n'
    output += Table.create(
        [(
            str(proof_copy),
            str(script(arr=proof_data)),
            script.name(),
            script.user()
        ) for script in scripts],
        ('Input', 'Output', 'Script', 'User'),
        use_ansi=use_ansi
    )
    output += '\nPlots\n-----\n\n'
    output += '![%s](%s.png)\n\n' % (title, filename)
    benchmarks = map(
        lambda n: benchmark(scripts, n),
        n_steps
    )
    results = [(n, result) for n, result in benchmarks]
    output += '%s\n----------\n\n' % title
    for n, result in results:
        output += 'N = %d\n------\n\n' % n
        output += benchmark_results(result, use_ansi=use_ansi) + '\n'

    plot = plot_results(results, title, loglog=True)
    return output, plot


def save_plot(plot, filename):
    plot.savefig('results/%s.png' % filename)


def save_benchmark_results(output, filename):
    if not os.path.isdir('results'):
        os.umask(0o002)
        try:
            os.mkdir('results')
        finally:
            os.umask(0)
    with open('results/%s.md' % filename, 'w') as f:
        f.write(output)
