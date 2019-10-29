
"""5.1
def check_fermat(a,b,c,n):
    if(n>2):
        if c^n == a^n + b^n :
            print('Holy smokes, Fermat was wrong')
        else:
            print("No,that doesn't work")


#check_fermat(3,4,5,3)
def take_input():
    a = int(input('Enter value of a:'))
    b = int(input('Enter value of b:'))
    c = int(input('Enter value of c:'))
    n = int(input('Enter value of n:'))
    check_fermat(a,b,c,n)


take_input()
"""

"""5.2
def is_triangle(a,b,c):
    if a + b >= c and a + c >= b and c + b >= a:
        print('Yes')
    else:
        print('No')


#is_triangle(1, 2, 3)


def take_input_triangle():
    a = int(input('Enter value for a:'))
    b = int(input('Enter value for b:'))
    c = int(input('Enter value for c:'))
    is_triangle(a, b, c)


take_input_triangle()
"""


