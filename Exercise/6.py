import math as ma
import time

def compare_func(x, y):
    """
    compares two values x and y and returns 1 if x is greater than or equal to y else returns -1
    :param x: An integer
    :param y: An integer
    :return:
    """
    if x > y or x == y:
        return 1
    else:
        return -1


a = compare_func(5, 4)
#print(a)


def distance(x1, y1,x2, y2):
    """
    Calculates distance between two points
    :param x1: x coordinate of first point
    :param y1: y coordinate of first point
    :param x2: x coordinate of second point
    :param y2: y coordinate of second point
    :return: Distance between first point and second point
    """
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = ma.sqrt(dsquared)
    return result


d = distance(1, 2, 4, 6)
#print('distance is', d)


def hypotenuse(a, b):
    """
    returns the length of hypotenuse
    :param a: length of side a
    :param b: length of side b
    :return: length of hypotenuse
    """
    length = a**2 + b**2
    return length


#hypotenuse(3, 4)


def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


start = time.time()
alpha = fibonacci(20)
diff = time.time() - start
print(diff, alpha)


def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers')
        return None
    elif n < 0:
        print('Factorial is only defined for positive integers')
        return None
    elif n == 0:
        return 1
    else:
        return n*factorial(n-1)


#factorial(-6)


def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod


def a(x, y):
    x = x + 1
    return x * y


def c(x, y, z):
    sum = x + y + z
    pow = b(sum)**2
    return pow


x = 1
y = x + 1
#print(c(x, y+3, x+y))


def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


#print(ack(1, 2))


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


#print(first('Noon'))
#print(last('Noon'))
#print(middle('babec'))


def is_palindrome(word):
    if (len(word) == 1 or len(word) == 2) and first(word) == last(word):
        #print('first and last letter matches ')
        return True
    elif first(word) == last(word):
        s = middle(word)
        #print(first(s), ' ', last(s))
        return is_palindrome(s)
    else:
        print('Not palindrome')
        return False


#print(is_palindrome('mom'))


def is_power(a1, b1):
    if a1 == 1 and int(a1/b1) == 0:
        return True
    elif a1 % b1 == 0 and is_power(a1/b1, b1):
        return True
    else:
        return False


# print(is_power(9, 3))
# print(is_power(10, 3))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# print(gcd(30, 90))


