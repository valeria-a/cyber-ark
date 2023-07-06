# def perf_log(other_func):
#
#     def wrapper(*args, **kwargs):
#
#         ret_val = other_func(*args, **kwargs)
#
#         return ret_val
#
#     return wrapper
import time

# long_running_func = perf_log(units='mili')(long_running_func)
def perf_log(units='sec'):
    def w(original_func):
        def wrapper(*args, **kwargs):
            start = time.time()
            ret_val = None
            try:
                ret_val = original_func(*args, **kwargs)
            finally:
                end = time.time()
                r = end - start
                if units == 'mili':
                    r *= 1000
                print(f'Function {original_func.__name__} took {r} {units}s')
                return ret_val
        return wrapper
    return w


@validate_range(start=20, end=30)
def foo(w:str, )

@perf_log(units='sec')
def long_running_func(num, iters):
  val = 1
  for i in range(iters):
    val = val * num
  return val

# long_running_func = perf_log(units='mili')(long_running_func)

if __name__ == '__main__':
    long_running_func(5, 100_000)