from table import Table


def display_benchmark_results(results):

    def headers():
        return 'avg', 'min', 'max', 'func', 'name'

    def row(result):
        return (
            "%.9f" % result.average(),
            "%.9f" % result.min(),
            "%.9f" % result.max(),
            result.name(),
            result.user()
        )

    rows = [row(result) for result in results]

    print(Table.create(rows, headers()))
