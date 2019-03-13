import time


def timer(f, kwargs):
    start = time.time()
    result = f(**kwargs)

    return time.time() - start if result is not False else -1
