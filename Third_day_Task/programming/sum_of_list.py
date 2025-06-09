from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

res_sum = reduce(lambda a, b: a + b, lst)

print("res_sum =", res_sum)
