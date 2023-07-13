import datetime
import math
from abc import ABC, abstractmethod
from functools import lru_cache


class FileSystemObject(ABC):
    def __init__(self, name):
        self.created_ts = datetime.datetime.now()
        self.name = name
        self.last_updated = self.created_ts

    @abstractmethod
    def get_size(self):
        pass

    def get_created_ts(self):
        return self.created_ts

    @abstractmethod
    def get_last_updated(self):
        pass

class File(FileSystemObject):

    def __init__(self, name, size_in_bytes):
        super().__init__(name)
        self.size_in_bytes = size_in_bytes

    def get_last_updated(self):
        return self.last_updated

    def get_size(self):
        return self.size_in_bytes

class Folder(FileSystemObject):

    def __init__(self, name):
        super().__init__(name)
        self._children: list[FileSystemObject] = []

    def add_child(self, file_system_obj: FileSystemObject):
        self._children.append(file_system_obj)
        self.get_size.cache_clear()

    def get_last_updated(self):
        pass

    @lru_cache
    def get_size(self):
        return sum(
            [child.get_size() for child in self._children])


@lru_cache
def my_fact(num):
    return math.factorial(num)

# l = [1,2, 3]
# @lru_cache
# def my_list_len(l):
#     return len(l)
# {l: 3}