# import sys
#
# num = 3
#
# print(sys.getsizeof(num))
# print(sys.getsizeof(23649574162792416479237649723864982364))
#
#
# num = 5
# print(id(num))
# num = 3.0
# print(id(num))
num = 5
# print(id(num))
#
# s1 = "a"
# print(id(s1))
# s2 = "a"
# print(id(s2))
# num = 5
# def foo(n):
#     print(id(n))
#     n = 0
#     print(id(n))
#     print(num)

# foo(num)
# print(id(num))

# num = 5
# def bar():
#     global num
#     num = 3
#
# bar()
# print(num)
print(5//2)
print(5/2)
print(5%2)
res = divmod(5, 2)
print(len(res))
# res[0] = 4

# l1 = [3,4,5]
# l2 = list()
# l1[0] = 4
#
# t1 = tuple(l1)

# l = [[1,1,1], [2,2], [3]]
# l[2] = []
# t = tuple(l)
# t[1][0] = "sdf"
# print(l)
# print(t)

# for elem in l:

seasons = ['summer', 'winter', 'autumn']
# for i in seasons:
#     print(i)
#
# for c in "Tel Aviv":
#     print(c)

city = "Tel Aviv"
# print(city[1:4])
# print(city[2:])
# print(city[:3])
# print(city[1::2])
# print(city[3:1])
# print(city[-3])
# print(city[-1])
# print(city[::-1])

sentence = "The sun is shining"
# print(sentence.split(' ')[-1][::-1])

# r = range(10, 1_000_000_000, 200)
# print(r)
# print(500 in r)
#
#
# for i in range(100, 50, -10):
#     print(i)
#
# d = {
#     'name': 'Valeria',
#     'city': 'netanya'
# }
#
# print(len(d))
#
# print(type(d))
# print(type(5))
#
# weekdays = {'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'}
# sport = {'mon', 'wed'}
# cyberark = {'tue', 'thu'}
# print(sport.intersection(cyberark))
# cyberark.add("fri")
#
# l = ['sun', 'mon', 'tue', 'wed', 'mon', 'sun']
# cyberark.update({2,3,4})
# print(cyberark)
# cyberark.pop()
# # print(list(set(l)))
#
# print(cyberark.union(sport))


# l = [1,2,3,4,5]
# for i, elem in enumerate(l):
#     if elem % 2 == 0:
#         l.append(elem-1)
#     if len(l) > 10:
#         break
# print(l)


# num: int = 5
# num = "dfgdfg"
# print(num)

# nums = [11,22, 33,44, 55, 66]
# a,b,c = nums
# print(a,b,c)
# a, *b = nums
# print(a,b)
# first, *_, last = nums
# print(first, last)
# print(_)
# *a, b, c, *d = nums

def foo(n1: int, n2: int, n3: int = 10, **kwargs):
    print(n1, n2, n3, kwargs)


def bar(*args, **kwargs):
    print(args)
    print(kwargs)
    foo(*args[:2], **kwargs)

# foo(2,3)
# bar(2,3,4,5, name='valeria', city='tel aviv')

# w1 = "asdasdad"
# w2 = 'dsd"fsdf'
# w3 = """
# Hello
# Hi
# Byw
# """
# print(f"My name is... {w1} \\n {{")
# print("asdada" + w1)
# # print(w3)
#
# l = ['a','p','p','l','e']
# t = "apple"
# print(type(*t))
# print("_".join(*t))

cities = ['new york', 'tel aviv', 'paris', 'london']
countries = ['us', 'israel']

# for c, cou, char in zip(cities, countries, 'abcd'):
#     print(c, cou, char)
    # print(city, country)

def filterA(elem):
    return 'a' in elem

res = filter(filterA, cities)
# print(res)
# for i in res:
#     print(i)
# print(tuple(res))
# a = map(str.title, res)
# for i in a:
#     print(i)
#
# for i in a:
#     print(i)

# res = map(lambda elem: elem.title() if len(elem) % 2 == 0 else elem.upper(), cities)