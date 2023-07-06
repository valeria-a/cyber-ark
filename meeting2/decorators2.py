import math


def greeting(other_func: callable):

    def wrapper(*args, **kwargs):
        print('hello')
        return other_func(*args, **kwargs)
    return wrapper

@greeting
def fact(n):
    # print(math.factorial(n))
    return math.factorial(n)


if __name__ == '__main__':
    print(fact(5))