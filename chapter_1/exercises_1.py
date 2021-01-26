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


# C-1.13	Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the opposite order than they were before, and compare this method to an equivalent Python function for doing the same thing.

# reverse_list(list):
# check list for length return empty list
# create empty list
# loop through org list starting from last index
# append to new list
# return list


def reverse_list(data, n):
    if n == 0:
        return False
    temp_list = []
    for i in range(n - 1, -1, -1):
        temp_list.append(data[i])

    return temp_list


# C-1.14	Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd.


def find_odd_pair(data):
    if len(data) < 2:
        return False
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            if i != j and data[i] != data[j]:
                product = data[i] * data[j]
                if product % 2 != 0:
                    return True

    return False


# Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct).


def is_unique(data):
    if len(data) == 0:
        return False
    elif len(data) == 1:
        return True
    num_set = set()
    for num in data:
        if num in num_set:
            return False
        else:
            num_set.add(num)
    return True


def is_unique_simple(data):
    if len(data) == 0:
        return False
    data_set = set(data)
    return len(data) == len(data_set)


# C-1.16	In our implementation of the scale function (page 25), the body of the loop executes the command data [j] *= factor. We have discussed that numeric types are immutable, and that use of the *= operator in this context causes the creation of a new instance (not the mutation of an existing instance). How is it still possible, then, that our implementation of scale changes the actual parameter sent by the caller?
