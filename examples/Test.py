#!/usr/bin/env python

# -----------------
# MatrixMultiply.py
# -----------------

print "MatrixMultiply.py"

import operator

def inner_product (a, b) :
    return sum(map(operator.mul, a, b))

def matrix_multiply (a, b) :
    return map(lambda r : map(lambda c : inner_product(r, c), zip(*b)), a)

a = [[1, 2, 3], [4, 5, 6]]
b = [[1, 2], [3, 4], [5, 6]]

c = matrix_multiply(a, b)
assert c == [[22, 28], [49, 64]]

c = matrix_multiply(b, a)
assert c == [[9, 12, 15], [19, 26, 33], [29, 40, 51]]

print "Done."
