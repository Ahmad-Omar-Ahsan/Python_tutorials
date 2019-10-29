import time as t

eng2esp = dict()
print(eng2esp)
eng2esp['one'] = 'uno'
print(eng2esp)
eng2french = {'one': 'un', 'two': 'deux', 'three': 'trois', 'four': 'quatre'}
print(eng2french)
print(eng2french['four'])
print(len(eng2french))
print('one' in eng2french)
print('un' in eng2french)
vals = eng2french.values()
print(vals)
print('un' in vals)
a = [1, 2, 3, 4]
print(1 in a)

print(eng2french.get('one', 0))


def histogram(s):
    d = dict()
    for c in s:
        b = d.get(c, 0)
        d[c] = b + 1
    return d


x = histogram('orangutan')
print(x)


def print_hist(x):
    list_dict = x.keys()
    sorted_list = sorted(list_dict)
    # print(sorted_list)
    for k in sorted_list:
        print(k, x[k])


print_hist(x)
# print(x.keys())


def rev_lookup(x, v):
    empty_rev = []
    for k in x:
        if x[k] == v:
            empty_rev.append(k)
    return empty_rev


keys = rev_lookup(x, 1)
print(keys)


def inv_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        inv.setdefault(val, [])
        inv[val].append(key)
    return inv


hist = histogram('parrot')
print(inv_dict(hist))

known = {0: 0, 1: 1}


def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res


start = t.time()
b = fibonacci(10)
diff = t.time() - start
print(diff, b)


def has_duplicates(li):
    d = histogram(li)
    for i in d:
        if d[i] > 1:
            return True
    return False


co = has_duplicates([1, 2, 3, 4, 5, 6, 7])
print(co)


def rotate_pairs(li):
    pass


# Exercise 11.1

def read_txt():
    fin = open(r'C:\Users\Ahmad Omar Ahsan\Documents\words.txt')
    d = dict()
    for line in fin:
        word = line.strip().lower()
        d[word] = word
    return d


p = read_txt()


