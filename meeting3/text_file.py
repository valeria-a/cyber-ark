import csv
import json
import os.path
from abc import ABC, abstractmethod

class TextFile(ABC):

    def __init__(self, file_path: str):
        # check path exists
        # chek file type
        # store the path
        if not os.path.exists(file_path):
            raise Exception()
        if os.path.splitext(file_path)[-1][1:] != self._get_ext():
            raise Exception()
        self._file_path = file_path

    def get_file_size(self):
        pass

    def get_content(self):
        with open(self._file_path, 'r') as fd:
            content = self._get_specific_content(fd)

        return content
        # open a file (fd / fh) - common for all
        # get content - specific

    @abstractmethod
    def _get_specific_content(self, fd):
        pass

    @abstractmethod
    def _get_ext(self):
        pass


class CsvFile(TextFile):

    def __init__(self, file_path, delimiter=','):
        super().__init__(file_path)
        self._delimiter = delimiter

    def get_rows(self):
        pass

    def _get_ext(self):
        return 'csv'

    def _get_specific_content(self, fd):
        ret_val = []
        for row in csv.DictReader(fd, delimiter=self._delimiter):
            ret_val.append(row)
        return ret_val

class TxtFile(TextFile):

    def _get_specific_content(self, fd):
        return fd.read()

    def _get_ext(self):
        return 'txt'

class JsonFile(TextFile):

    def is_object(self):
        pass

    def _get_specific_content(self, fd):
        return json.load(fd)

    def _get_ext(self):
        return 'json'

class TextFileFactory:
    @staticmethod
    def get_file_mngr(filename):
        name, ext = os.path.splitext(filename)
        match ext:
            case '.csv':
                return CsvFile(filename)
            case '.json':
                return JsonFile(filename)
            case '.txt':
                return TxtFile(filename)
            case _:
                raise ValueError('Unsupported file extension')

if __name__ == '__main__':
    f = ['a.json', 'b.txt', 'c.csv']
    a = JsonFile('sdfsdf.json')
    b = CsvFile('sdfsdf.csv')
    mngrs = []
    for i in f:
        mngrs.append(TextFileFactory.get_file_mngr(i))
    for m in mngrs:
        pass

