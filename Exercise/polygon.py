import TurtleWorld
import math as m

world = TurtleWorld.TurtleWorld()
bob = TurtleWorld.Turtle()
print(bob)
"""
for i in range(4):
    print ('Hello!')

for num in range(4):
   fd(bob, 100)
  rt(bob)
"""


def square(t, length):
    """ Draw a square with sides of given length
    :param t:
    :param length:
    :return: returns the turtle to staring position or location
    """
    for num in range(4):
        TurtleWorld.fd(t, length)
        TurtleWorld.rt(t)


def polyline(t, n, length, angle):
    for i in range(n):
        TurtleWorld.fd(t, length)
        TurtleWorld.rt(t, angle)


def polygon(t, length, n):
    """ Draws a polygon with n sides

    :param t: Turtle
    :param length: length of each side
    :param n: number of sides
    :return:
    """
    angle = 360 / n
    polyline(t, n, length, angle)


# polygon(bob,100,6)

def circle(t, r):
    """
     Draws a circle with given radius
    :param t: turtle
    :param r: radius
    :return:
    """
    circumference = 2 * m.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, length, n)


def arc(t, r, angle):
    arc_length = 2 * m.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


#square(bob, 150)
#polygon(bob, 100, 6)
#bob.delay = 0.01
#circle(bob, 50)
#arc(bob, 100, 90)


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    TurtleWorld.fd(t, length*n)
    TurtleWorld.lt(t, angle)
    draw(t, length, n-1)
    TurtleWorld.rt(t, 2*angle)
    draw(t, length, n-1)
    TurtleWorld.lt(t, angle)
    TurtleWorld.bk(t, length*n)


draw(bob, 10, 10)
TurtleWorld.wait_for_user()

