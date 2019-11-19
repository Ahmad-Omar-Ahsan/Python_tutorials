
class Time(object):
    """
    represents the time of the day. Attributes: hour, ,minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' %(self.hour, self.minute, self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes*60 + self.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def __radd__(self, other):
        return self.__add__(other)


start = Time()
start.hour = 9
start.minute = 45
start.second = 00


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


end = start.increment(1337)
# print(end.is_after(start))

time = Time(9, 45, 45)


class Point(object):
    """
    represents a point in 2D space
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x = %d, y = %d' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other,Point):
            poi = Point()
            poi.x = self.x + other.x
            poi.y = self.y + other.y
            return poi
        else:
            poi = Point()
            poi.x = self.x + other[0]
            poi.y = self.y + other[1]
            return poi


p = Point(23, 45)
p1 = Point(45, 43)

#print(p)
#print(p + p1)
#print(end)

start = Time(8, 45)
duration = Time(1, 45)
#print(start + duration)
#print(1000 + start)


def print_attributes(obj):
    for attr in obj.__dict__:
        print(attr, getattr(obj, attr))


class Kangaroo(object):
    """
    Class for Kangaroo
    """

    def __init__(self, contents=None):
        if contents == None:
            contents = []
        self.pouch_contents = contents

    def put_in_pouch(self, item):
        """

        :param item: object or any other data type
        :return:
        """
        self.pouch_contents.append(item)

    def __str__(self):
        t = [object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = '   ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)


kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
print(' ')
print(roo)