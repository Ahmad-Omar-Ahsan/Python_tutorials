# 12.1
import random as rd
import operator
t = ('a', 'b', 'c', 'd', 'e')
# print(t)
t1 = (1,)
# print(type(t1))
t2 = 1
# print(type(t2))
t = tuple('lupins')
# print(t)
# print(t[1:3])
t = ('B',) + t[1:]
# print(t)

# 12.2
a, b = 10, 15
# print(a, b)
a, b = b, a
# print(a, b)
addr = 'monty@python.org'
uname, domain = addr.split('@')
# print(uname, domain)


# 12.3
quotient, remainder = divmod(6, 3)
# print(quotient, remainder)


def min_max(x, y):
    return min(x, y), max(x, y)


def print_all(required, optional=0, *args):
    print(required, optional, args)


# print_all(1, 2.4, 'Omar', [1, 2, 3, 4], {40: 'CSE'})

t = (2, 1)
# print(divmod(*t))


def sumall(*t):
    c = 0
    for i in range(len(t)):
        c += t[i]
    return c


d = sumall(1, 2, 3, 4)
print(d)

s = 'abc'
t = [0, 1, 2]
d = list(zip(s, t))
print(d)
for letter, number in d:
    print(letter, number)


def has_match(t1, t2):
    for x, y in list(zip(t1, t2)):
        if x == y:
            return True
    return False


for index, element in enumerate('abc'):
    print(element)

d = {'a': 0, 'b': 1, 'c': 2}
key = d.keys()
item = d.items()
#print(item)
#print(key)
t = item
d = dict(zip('abc', range(7)))
print(d)
#print(t)
d = dict(t)
#print(d)

# print((0, 1, 2000000) < (0, 1, 4))

# 12.2


def sort_by_length(words):
    t = []
    for word in words:
        t.append(len(word), words)
    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res


# 12.3


def most_frequent(s):
    d = dict()
    for letter in s:
        b = d.get(letter, 0)
        d[letter] = b + 1
    key_item = d.items()
    sorted_x = sorted(key_item, reverse=True, key=lambda kv: kv[1])
    return sorted_x


p = most_frequent('banana')
# 12.5

fin = open(r'C:\Users\Ahmad Omar Ahsan\Documents\words.txt')
list_of_words = list()
for line in fin:
    word = line.strip()
    list_of_words.append(word)


def find_index(word, c):
    for i in range(len(word)):
        if word[i] == c:
            return i
    return False


def is_reducible(t):
    empty = []
    for i in range(len(t)):
        if t[i] in list_of_words:
            empty.append(t[i])
    return empty


def valid_words(s):
    t = []
    for c in s:
        word = s
        x = find_index(word, c)
        new_s = word[:x] + word[x+1:]
        # print(new_s)
        t.append(new_s)
    b = list()
    for value in t:
        p = value.lower()
        b.append(p)
    reducible = is_reducible(b)
    print(reducible)
    for s in reducible:
        valid_words(s)


valid_words('Sprite')












