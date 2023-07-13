class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
            cls._instances[cls].instance = lambda: cls._instances[cls]
        return cls._instances[cls]

class MyLogger(metaclass=SingletonMeta):
    pass
class Cache(metaclass=SingletonMeta):

    def __init__(self):
        self._cache = {}

    def set(self, key, item):
        pass


if __name__ == '__main__':
    c = Cache()
    print(Cache())
    print(Cache())
    c = Cache()
    print(c)
    print(c.instance())
    l = MyLogger()
    print(SingletonMeta._instances)


# class A:
#     def __call__(self, *args, **kwargs):
#         pass

#
# mya = A()
# mya()
#
#
# class Plot:
#     def draw_plot(self):
#         passs
#
# my_plot = Plot()
# my_plot([])