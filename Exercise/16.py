import copy

class Time(object):
    """
    represents the time of the day
    attributes: hour, minute, second
    """


time = Time()
time.hour = 11
time.minute = 59
time.second = 30

print(time)


def print_time(t):
    print('%.2d:%.2d:%2d' % (t.hour, t.minute, t.second))


def is_after(t1, t2):
    a = 3600*t1.hour + 60*t1.minute + t1.second
    b = 3600 * t2.hour + 60 * t2.minute + t2.second
    return a > b


m = Time()
m.hour = 12
m.minute = 34
m.second = 59


n = Time()
n.hour = 10
n.minute = 12
n.second = 23

l = is_after(m, n)
print(l)


def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    return sum


start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
print_time(done)


def increment(time, seconds):
    s = seconds % 60
    m = seconds / 60
    time.seconds += s
    time.minute += m
    if time.minute >= 60:
        time.minute -= 60
        time.hoour += 1


def increment(time, seconds):
    t = copy.deepcopy(time)
    print('Original time was: ', print_time(time))

    t.second += seconds
    if t.second >= 60:
        quotient, remainder = divmod(t.second, 60)
        t.second = remainder
        t.minute += quotient
    if t.minute >= 60:
        quotient, remainder = divmod(t.minute, 60)
        t.minute = remainder
        t.hour += quotient
    if t.hour >= 13:
        t.hour -= 13

    return t


p = increment(start, 123123)
print('New time is: ', print_time(p))


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


print(time_to_int(int_to_time(10000000)) == 10000000)


def valid_time(time):
    if time.hours < 0 or time.minutes < 0 or time.seconds < 0:
        return False
    if time.minutes >= 60 or time.seconds >= 60:
        return False
    return True


def add_time(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


