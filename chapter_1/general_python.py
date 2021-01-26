def square_list(n):
    squares = []
    for k in range(1, n + 1):
        squares.append(k * k)
    return squares


def general_list_comprehension(n, comp_type="list"):
    if comp_type.lower() == "list":
        squares = [k * k for k in range(1, n + 1) if n % k == 0]
    elif comp_type.lower() == "set":
        squares = {k * k for k in range(1, n + 1)}
    elif comp_type.lower() == "generator":
        squares = (k * k for k in range(1, n + 1))
    elif comp_type.lower() == "dictionary":
        squares = {k: k * k for k in range(1, n + 1)}

    return squares


def sum_of_first_n_squares(n):
    return sum(k * k for k in range(1, n + 1))


def print_divmod(a, b):
    x = divmod(a, b)
    quotent, remainder = x
    print(quotent, remainder)
    return quotent, remainder


def print_iterative():
    for x, y in [(7, 2), (5, 8), (6, 4)]:
        print(f"x: {x}, y: {y}")


def fibonacci(n):
    a, b = 0, 1
    i = 0
    while i < n:
        yield a
        a, b = b, a + b


# print(fibonacci(10))
# print(square_list(10))
# print(general_list_comprehension(10))
# print(general_list_comprehension(10, "set"))
# print(general_list_comprehension(10, "generator"))
# print(general_list_comprehension(10, "dictionary"))
# print(sum_of_first_n_squares(10))
# print(print_divmod(10, 40))
# print(print_iterative())
