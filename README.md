# Python Script Benchmark Tools

Benchmark script run times, print tables of results and display plots.

## Install

`pip install script_benchmark_tools`

##

See examples folder for usage.

## Sample Output


Proofs
------
insertion_sort [1, 2, 3, 4, 5, 6]
selection_sort [1, 2, 3, 4, 5, 6]

Benchmarks
----------
N = 10
------
|  min          |  avg          |  max          |  func            |  name     |
|---------------|---------------|---------------|------------------|-----------|
|  0.000008106  |  0.000018342  |  0.000201225  |  insertion_sort  |  sarcoma  |
|  0.000008821  |  0.000029361  |  0.001542091  |  selection_sort  |  sarcoma  |

N = 50
------
|  min          |  avg          |  max          |  func            |  name     |
|---------------|---------------|---------------|------------------|-----------|
|  0.000027895  |  0.000030518  |  0.000068188  |  insertion_sort  |  sarcoma  |
|  0.000089884  |  0.000214245  |  0.004812956  |  selection_sort  |  sarcoma  |

N = 100
------
|  min          |  avg          |  max          |  func            |  name     |
|---------------|---------------|---------------|------------------|-----------|
|  0.000061750  |  0.000069265  |  0.000296116  |  insertion_sort  |  sarcoma  |
|  0.000331640  |  0.000390785  |  0.000853777  |  selection_sort  |  sarcoma  |

N = 500
------
|  min          |  avg          |  max          |  func            |  name     |
|---------------|---------------|---------------|------------------|-----------|
|  0.000585079  |  0.000774384  |  0.005968094  |  insertion_sort  |  sarcoma  |
|  0.008999825  |  0.015488691  |  0.050533056  |  selection_sort  |  sarcoma  |

N = 1000
------
|  min          |  avg          |  max          |  func            |  name     |
|---------------|---------------|---------------|------------------|-----------|
|  0.001787901  |  0.009231312  |  0.057305098  |  insertion_sort  |  sarcoma  |
|  0.037415981  |  0.047663388  |  0.092668772  |  selection_sort  |  sarcoma  |

![Benchmark Plot](https://github.com/sarcoma/python-script-benchmark-tools/blob/master/examples/benchmark.png)
