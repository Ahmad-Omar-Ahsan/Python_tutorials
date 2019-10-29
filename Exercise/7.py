#7.1
import math as m


def print_n(s, n):
    while n > 0:
        print(s)
        n = n - 1
    return


# print_n('Omar', 5)

"""while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
"""

# print('Done! ')


# epsilon = 0.0000000000001


def square_root(a, x):
    epsilon = 0.000000000001
    while True:
        # print(x)
        y = (x + a/x)/2
        if abs(x - y) < epsilon:
            return y
        x = y


# square_root(10, 4)


def test_square_root():
    for i in range(1, 10):
        a = float(i)
        actual = m.sqrt(a)
        estimate = square_root(a, 5)
        difference = abs(actual - estimate)
        print(a, estimate, actual, difference)


# test_square_root()


def eval_loop():
    while True:
        user_prompt = input('Please enter into your value:')
        if user_prompt == 'done':
            return e
        e = eval(user_prompt)
        print(e)


# p = eval_loop()
# print(p)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def estimate_pi():
    s = 0
    epsilon = 1e-15
    actual = m.pi
    i = 0
    factor = (2 * m.sqrt(2) / 9801)
    total = 0
    while True:
        num = factorial(4*i) * (1103 + 26390*i)
        den = factorial(i)**4 * 396**(4*i)
        term = factor * num / den
        total = total + term
        if abs(total) < epsilon:
            break
        i = i + 1
    return 1/total


estimate = estimate_pi()
actual = m.pi
diff = abs(actual - estimate)