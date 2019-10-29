import random as rad
import time
import numpy as np

cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
# print(cheeses, numbers, empty)

numbers = [17, 25]
numbers[1] = 5
# print(numbers)

# print('Edam' in cheeses)
# print('Brie' in cheeses)


a = [1, 2, 3]
b = [4,5,6]
c = a + b
# print(c)
# print(a*3)

t = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t[1:3])
# print(t[:4])
# print(t[::-2])
t[1:3] = ['x', 'y']
# print(t)
num = [0, 1, 2, 3, 4, 5]
# print(num[4::-2])

x = ['a', 'b', 'c']
x.append('d')
# print(x)

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
# print(t1)

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
# print(t)


def add_all(t):
    total = sum(t)
    return total


total = add_all(numbers)
# print(total)


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


p = capitalize_all(t)
# print(p)


# Exercise 10.1
def cumulative_sum(t):
    res = []
    for i in range(len(t)):
        res.append(sum(t[0:i+1]))
    return res


num = [1, 2, 3]
res = cumulative_sum(num)
print(res)


t = ['a', 'b', 'c']
x = t.pop(1)
# print(t)
# print(x)


t = ['a', 'b', 'c']
del t[1]
# print(t)


t = ['a', 'b', 'c', 'd', 'e']
del t[1:5]
# print(t)

s = 'spam'
t = list(s)
# print(t)

s = 'pining for the fjords'
t = s.split()
# print(t)
delimiter = ' '
# print(delimiter.join(t))


s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
# print(t)


a = [1, 2, 3]
b = a

# print(a is b)

b[0] = 19
# print(a)


#10.2

def chop(t):
    del t[0]
    del t[-1]


def middle(t):
    return t[1:-1:]


t = ['a', 'b', 'c', 'd', 'e']
x = middle(t)
# print(x)


# 10.3
def is_sorted(t):
    orig = t[:]
    t.sort()
    if t == orig:
        return True
    else:
        return False


t = ['b', 'a']
# print(is_sorted(t))


# 10.4
def is_anagram(s1, s2):
    s1 = sorted((s1.lower()))
    s2 = sorted(s2.lower())
    if s1 == s2:
        return True
    else:
        return False


# print(is_anagram('Omar', 'Roma'))


# 10.5
def has_duplicates(t):
    c = 0
    for i in range(len(t)):
        z = t[i]
        for j in range(i + 1, len(t)):
            if z == t[j]:
                c = c + 1
    # print(c)
    return c


t = [6, 2, 3, 4, 5, 1, 3]
print(has_duplicates(t))


p = np.pi
birthday = []
for i in range(0, 23):
    x = rad.randint(1, 31)
    birthday.append(x)

# print(birthday)
b = has_duplicates(birthday)
# print(round(b/31 * 100, 2))


# 10.6
def remove_duplicates(t):
    orig = t[:]
    c = 0
    for i in range(0, len(orig)):
        if i >= len(orig) - c:
            break
        z = orig[i]
        print('i: ' + str(i))
        for j in range(i + 1, len(orig)):
            if j >= len(orig) - c:
                break
            if z == orig[j]:
                print('orig[j]: ' + str(orig[j]))
                del orig[j]
                c = c + 1
        print(orig)


# 10.7
empty = []
def file_in_mod1():
    fin = open(r'C:\Users\Ahmad Omar Ahsan\Documents\words.txt')
    for line in fin:
        word = line.strip()
        empty.append(word)
    return empty


def file_in_mod2():
    fin = open(r'C:\Users\Ahmad Omar Ahsan\Documents\words.txt')
    pat = []
    for line in fin:
        word = line.strip()
        pat = pat + [word]
    return pat


# 10.8
def bisect(target):
    lots = file_in_mod1()
    length = len(lots)
    l = 0
    r = length - 1
    while l <= r:
        m = int((r + l)/2)
        if lots[m] == target:
            return m
        elif lots[m] < target:
            l = m + 1
        else:
            r = m - 1


p = bisect('abductors')
print(p)


def is_reverse(word1, word2):
    if len(word1) !=  len(word2):
        return False
    i = 0
    j = len(word2) - 1
    while j >= 0:
        # print(i, j)
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    return True


def rev(w):
    return w[::-1]


# 10.9
def reverse_pair():
    lots = file_in_mod1()
    empty = []
    for i in range(len(lots)):
        word = rev(lots[i])
        if bisect(word):
            empty.append(word)
    print(empty)


# reverse_pair()


# 10.10
file_in_mod1()
print(empty)







