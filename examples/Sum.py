#!/usr/bin/env python

# ------
# Sum.py
# ------

import operator
import sys
import time

def sum_1 (a) :
    if not a :
        return 0
    else :
        return a[0] + sum_1(a[1:])

def sum_2 (a) :
    s = 0
    i = 0
    while i != len(a) :
        s += a[i]
        i += 1
    return s

def sum_3 (a) :
    s = 0
    for i in range(len(a)) :
        s += a[i]
    return s

def sum_4 (a) :
    s = 0
    p = iter(a)
    while True :
        try :
            s += p.next()
        except StopIteration :
            break
    return s

def sum_5 (a) :
    s = 0
    for v in a :
        s += v
    return s

def sum_6 (a) :
    return reduce(operator.add, a, 0)

def sum_7 (a) :
    try :
        p = iter(a)
        return p.next() + sum_7(p)
    except StopIteration :
        return 0

def test_1 (f, c) :
    assert f(c())          == 0
    assert f(c([2]))       == 2
    assert f(c([2, 3]))    == 5
    assert f(c([2, 3, 4])) == 9

def test_2 (f, c, s) :
    print f.__name__ + " (" + s + ")"
    b = time.clock()
    assert f(500 * [1]) == 500
    e = time.clock()
    print "%5.3f" % ((e - b) * 1000), "milliseconds"
    print

print "Sum.py"
print

test_1(sum_1, list)
test_1(sum_1, tuple)
#test_1(sum_1, set) # TypeError: 'set' object does not support indexing

test_1(sum_2, list)
test_1(sum_2, tuple)
#test_1(sum_2, set) # TypeError: 'set' object does not support indexing

test_1(sum_3, list)
test_1(sum_3, tuple)
#test_1(sum_3, set) # TypeError: 'set' object does not support indexing

test_1(sum_4, list)
test_1(sum_4, tuple)
test_1(sum_4, set)

test_1(sum_5, list)
test_1(sum_5, tuple)
test_1(sum_5, set)

test_1(sum_6, list)
test_1(sum_6, tuple)
test_1(sum_6, set)

test_1(sum_7, list)
test_1(sum_7, tuple)
test_1(sum_7, set)

test_1(sum,   list )
test_1(sum,   tuple)
test_1(sum,   set)

print sys.version
print

test_2(sum_1, list,  "recursion")
test_2(sum_2, list,  "while")
test_2(sum_3, list,  "for in range")
test_2(sum_4, list,  "while iter")
test_2(sum_5, list,  "for in")
test_2(sum_6, list,  "reduce")
test_2(sum_7, list,  "recursion iter")
test_2(sum,   list,  "")

print "Done."
