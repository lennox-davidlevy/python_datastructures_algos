import random

# R-1.1	Write a short Python function, is_multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.


def is_multiple(n=None, m=None):
    if n == None or m == None:
        return False
    return n % m == 0


# R-1.2	Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.


def is_even(k=None):
    if k == None:
        return False
    return k ^ 1 == k + 1


# R-1.3	Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.


def minmax(data):
    if len(data) == 0:
        return False
    minumum = float("inf")
    maximum = float("-inf")
    for num in data:
        if num <= minumum:
            minumum = num
        if num >= maximum:
            maximum = num
    return (minumum, maximum)


# Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.


def sum_of_squares(n=None):
    if n <= 0 or n == None:
        return 0
    return sum([i * i for i in range(0, n + 1)])


# R-1.6	Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.


def sum_of_odd_squares(n=None):
    if n <= 0 or n == None:
        return 0
    sum_of_odds = 0
    for i in range(0, n + 1):
        if i % 2 != 0:
            sum_of_odds += i * i

    return sum_of_odds


def sum_of_odd_squares_one_line(n=None):
    if n <= 0 or n == None:
        return 0
    return sum([i * i for i in range(0, n + 1) if i % 2 != 0])


# R-1.8	Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references the same element?


def find_pos_index(data, n, k):
    if n == 0 or abs(k) > n:
        return False
    return data[n + k]


# R-1.9	What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80?
for i in range(50, 90, 10):
    # print(i)
    pass

# What parameters should be sent to the range constructor, to produce a range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

for i in range(8, -10, -2):
    # print(i)
    pass

# R-1.11	Demonstrate how to use Python's list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

list_by_two = [pow(2, x) for x in range(1, 9)]
# print(list_by_two)
# R-1.12	Python's random module includes a function choice(data) that returns a random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to the built-in range function, that return a random choice from the given range. Using only the randrange function, implement your own version of the choice function.


def home_made_choice(data, n):
    return data[random.randrange(0, n)]
