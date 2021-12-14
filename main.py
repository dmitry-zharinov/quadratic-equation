from modules.quadratic import quadratic


def solve_quadratic():
    print("ax^2 + bx + c = 0")
    print("Please enter coefficients a, b, c (or 'x' to exit):")

    while True:
        a = input("a = ")
        if a == "x":
            print("Goodbye.")
            break
        b = input("b = ")
        c = input("c = ")

        result = quadratic(a, b, c)
        print(f'Result: x = {result}')


if __name__ == '__main__':
    solve_quadratic()
