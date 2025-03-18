# write a program that finds a maximum value from a list using reduce function

from functools import reduce

l = [1, 2, 3, 54, 453,34232, 123131214, 32432]

def maximum(a, b):
    if (a>b):
        return a
    return b


print(reduce(maximum,l))