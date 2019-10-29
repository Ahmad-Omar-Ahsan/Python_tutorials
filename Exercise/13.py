import random
import string

for i in range(10):
    x = random.random()
    # print(x)

print(random.randint(5, 10))

t = 1, 2, 3
print(random.choice(t))


def histogram(s):
    d = dict()
    for c in s:
        b = d.get(c, 0)
        d[c] = b + 1
    return d


t = 'aab'
h = histogram(t)
print(h)


def choose_from_hist(d):
    c = 0
    t1 = []
    for key in d:
        c = c + d[key]
        t1.append(d[key])


fin = open(r'C:\Users\Ahmad Omar Ahsan\Documents\demo.txt')


def process_line(line, h):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        h[word] = h.get(word, 0) + 1


def process_file(fin):
    h = dict()
    for line in fin:
        process_line(line, h)
    return h


def total_words(h):
    return sum(h.values())


def different_words(h):
    return len(h)


hist = process_file(fin)
print(hist)

print(total_words(hist))
print(different_words(hist))


def most_common(h):
    t = []
    for key, value in h.items():
        t.append((value, key))
    t.sort(reverse=True)
    return t


def print_most_common(h, num=10):
    t = most_common(h)
    print('The most common words are: ')
    for freq, word in t[0: num]:
        print(word, '\t', freq)


print_most_common(hist, 20)


def read_txt():
    fp = open(r'C:\Users\Ahmad Omar Ahsan\Documents\words.txt')
    d = dict()
    for line in fp:
        word = line.strip().lower()
        d[word] = word
    return d


p = read_txt()


def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res


diff = subtract(hist, p)


def cumulative_sum(d):
    res = []
    c = 0
    for key in d:
        c = c + d[key]
        res.append(c)
    return res


cum_sum = cumulative_sum(hist)
print(cum_sum)

n = cum_sum[-1]
print(n)
x = random.randint(1, n)
print(x)


