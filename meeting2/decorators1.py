import math
from functools import wraps


def greeting(other_func: callable):

    @wraps(other_func)
    def wrapper():
        print('hello')
        other_func()
    return wrapper
#
@greeting
def dup():
    """
    prints the number x 2
    :return:
    """
    n = int(input("insert a num"))
    print(n*2)
# dup = greeting(dup)
# dup()


def fact():
    n = int(input("insert a num"))
    print(math.factorial(n))


# foo = fact
# foo()

if __name__ == '__main__':
    print(dup.__name__)
    print(dup.__doc__)
    dup()

