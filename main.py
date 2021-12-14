from square_root import square_root

print("Please enter a, b, c.")

while True:
    a = input("a = ")
    if a == "x":
        print("Good bye.")
        break
    b = input("b = ")
    c = input("c = ")

    result = square_root(a, b, c)
    print(f'Result: x = {result}')

    
if __name__ == '__main__':
    square_root()