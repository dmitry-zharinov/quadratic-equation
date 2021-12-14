from modules.quadratic_equation import solve_equation

print("Please enter a, b, c.")
print("ax^2 + bx + c = 0")

while True:
    a = input("a = ")
    if a == "x":
        print("Good bye.")
        break
    b = input("b = ")
    c = input("c = ")

    result = solve_equation(a, b, c)
    print(f'Result: x = {result}')


if __name__ == '__main__':
    solve_equation()
