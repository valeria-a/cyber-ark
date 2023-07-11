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

    def _get_specific_content(self, fd):
        return json.load(fd)

    def _get_ext(self):
        return 'json'

csv_file = CsvFile("/Users/valeria/src/morning-ninjas/lesson9/files/data/files_ex/username-or-email.csv", ';')
txt = TxtFile("/Users/valeria/src/morning-ninjas/lesson9/files/data/alice_in_wonderland.txt")
json_file = JsonFile("/Users/valeria/src/morning-ninjas/lesson9/files/data/my_persons.json")
files_list = [csv_file, txt, json_file]
for f in files_list:
    print(f.get_content())

# csv_file = CsvFile("/Users/valeria/src/morning-ninjas/lesson9/files/data/AAPL.csv")

