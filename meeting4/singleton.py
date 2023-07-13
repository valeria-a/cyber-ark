# class Singleton:
#     __instance = None
#
#     @staticmethod
#     def instance():
#         if not Singleton.__instance:
#             Singleton.__instance = Singleton()
#         return Singleton.__instance
#
#     # def __new__(cls, *args, **kwargs):
#     #     pass
#
#     def __init__(self):
#         if Singleton.__instance:
#             raise Exception("This class is a singleton!")
#         else:
#             Singleton.__instance = self
from threading import Lock


class Singleton:
    _instance = None
    _lock = Lock()

    # class method, hence works like instance() static method
    def __new__(cls):
        print('inside new')
        if cls._instance is None:
            with Singleton._lock:
                if cls._instance is None:
                    print('Creating the object')
                    cls._instance = super().__new__(cls)
        return cls._instance

if __name__ == '__main__':
    s = Singleton()
    print(s)
    # s = Singleton.instance()
    # print(s)
    s = Singleton()
    print(s)


