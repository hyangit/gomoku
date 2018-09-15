import time
import functools


def time_cost(fn):
    @functools.wraps(fn)
    def _wrapper(*args, **kwargs):
        start = time.clock()
        r = fn(*args, **kwargs)
        print("%s cost %s second" % (fn.__name__, time.clock() - start))
        return r

    return _wrapper


