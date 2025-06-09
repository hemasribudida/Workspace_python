from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = list(filter(lambda x: x % 2 == 0, lst))  # [2, 4, 6, 8]


squares = list(map(lambda x: x * x, evens))      # [4, 16, 36, 64]

sum_of_squares = reduce(lambda a, b: a + b, squares)


print(sum_of_squares)
