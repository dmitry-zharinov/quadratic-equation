import math


def solve_equation(a, b, c):
    if a == 0:
        raise Exception('a must be <> 0')
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return (x1, x2)
    elif discr == 0:
        x = -b / (2 * a)
        return x
    else:
        return None
