import time


def timer(f, kwargs):
    start = time.time()
    f(**kwargs)

    return time.time() - start
