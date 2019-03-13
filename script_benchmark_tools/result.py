from script_benchmark_tools.script import Script


class Result:

    def __init__(self, script: Script, run_times, n_runs):
        self._n_runs = n_runs
        self._run_times = run_times
        self._script = script

    def __repr__(self):
        return "%.9f | %.9f | %.9f | %d | %s | %s" % (
            self.average(),
            self.min(),
            self.max(),
            self.n_runs(),
            self._script.name(),
            self._script.user()
        )

    def n_runs(self):
        return self._n_runs

    def name(self):
        return self._script.name()

    def user(self):
        return self._script.user()

    def kwargs(self):
        return self._script.kwargs()

    def min(self):
        return min(self._run_times)

    def max(self):
        return max(self._run_times)

    def average(self):
        return sum(self._run_times) / self._n_runs
