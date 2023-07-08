import math


def greeting(other_func: callable):
    print('defining greeting wrapper')
    def wrapper(*args, **kwargs):
        print('running greeting wrapper')
        print('hello')
        ret_val =  other_func(*args, **kwargs)
        print('greeting',ret_val)
        return ret_val
    return wrapper

def always_float(other_func: callable):
    print('defining always_float wrapper')
    def wrapper(*args, **kwargs):
        print('running always_float wrapper')
        return float(other_func(*args, **kwargs))
    return wrapper

@always_float
@greeting
def fact(n):
    # print(math.factorial(n))
    return math.factorial(n)
# fact = greeting(always_float(fact))

if __name__ == '__main__':
    print(fact(5))