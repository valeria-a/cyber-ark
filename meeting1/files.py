# f = open('my_data.txt')
# content = f.read()
# f.close()
import json
import os.path
import sys
from io import TextIOWrapper

with open('my_data.txt') as f:
    for line in f:
        print(line, end="")
    # print(type(f))
    # content = f.read()
    # print(content)


# with open('data.json') as f:
#     content = f.read()
#     print(content)
#     content = json.loads(content)
#     print(content['n1'])

def foo(file_name):
    f1 = "data/"
    f2 = "/local"
    path = f"{f1}/{f2}/{file_name}"
    os.path.join(f1, f2, file_name)
    os.path.sep