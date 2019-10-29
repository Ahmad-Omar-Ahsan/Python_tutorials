import math as m
import copy
from World import World

class Point(object):
    """
    represents a  point in 2-D space
    """


print(Point)
blank = Point()
b2 = Point()
print(blank)

blank.x = 3
blank.y = 4
b2.x = 8
b2.y = 9
x = blank.x
print(x)


def print_point(p):
    print(p.x, p.y)


print_point(blank)


def distance(p1, p2):
    d1 = (p1.x - p2.x)**2
    d2 = (p2.y - p1.y)**2
    dist = m.sqrt(d1 + d2)
    print(dist)


distance(blank, b2)


class Rectangle(object):
    """
        represents a rectangle.
        attributes: width, height, corner
    """


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


def find_center(box):
    p = Point()
    p.x = box.corner.x + box.width/2.0
    p.y = box.corner.y + box.height/2.0
    return p


center = find_center(box)
print_point(center)


def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight


print(box.width)
print(box.height)
grow_rectangle(box, 50, 100)
print(box.width)
print(box.height)


def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy


box2 = copy.deepcopy(box)
print(box2 is box)
print(box2.corner is box.corner)


def move_rectangle():
    r = Rectangle()
    return r


world = World()
canvas = world.ca(width=500, height=500, background='white')
bbox = [[-150, -100], [150, 100]]
canvas.rectangle(bbox, outline='black', width=2, fill='green4')
canvas.circle([-25, 0], 70, outline=None, fill='red')
world.mainloop()

