# def letter_gen():
#     yield 'a'
#     print('after a')
#     yield 'b'
#     print('after b')
#     yield 'c'

def letter_gen(first, last):
    curr = first
    while ord(curr) <= ord(last):
        yield curr
        curr = chr(ord(curr)+1)


# r = letter_gen()
# print(r)
#
# print(next(r))
# print('aaaaaaaaaaaaa')
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))

for letter in letter_gen('r', 'w'):
    print(letter)