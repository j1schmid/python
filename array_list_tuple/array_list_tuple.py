#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys

import numpy as np

# cite: https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples
# Tuples have structure, lists have order.
#
# https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples
# That also means that you can't delete an element or sort a tuple. However, you
# could add new element to both list and tuple with the only difference that you
# will change id of the tuple by adding element.


someTuple = (1,2,'Im a tuple')
someList = [3,4,'Im a list']
someArray = np.array([1,3,'Im a numpy array'])



# Tuples

# Tuples are immutable; you can't change which variables they contain after 
# construction. However, you can concatenate or slice them to form new tuples:
print('type(someTuple) returns: {}'.format(type(someTuple)))
print('someTuple:\n{}'.format(someTuple))
print('someTuple[2]: {}'.format(someTuple[2]))

a = (1, 2, 3) # creata a tuple containing integers
b = a + (4, 5, 6) # add some elements to a tuple
c = b[1:] # copy some elements of a tuple

name = "Joe"
age = 40
location = "New York"
joe = (name, age, location) # store objects in a tuple

print('type(tuple(someList)) returns: {}'.format(type(tuple(someList))))
print('type(tuple(someArray)) returns: {}'.format(type(tuple(someArray))))



# List

print('type(someList) returns: {}'.format(type(someList)))
print('someList:\n{}'.format(someList))
print('someList[2]: {}'.format(someList[2]))

someList.append('Append element to a list')
print('type(someList) returns: {}'.format(type(someList)))
print('someList:\n{}'.format(someList))

someList += ['add']
print('type(someList) returns: {}'.format(type(someList)))
print('someList:\n{}'.format(someList))



# Numpy array

print('type(someArray) returns: {}'.format(type(someArray)))
print('someArray:\n{}'.format(someArray))
print('someArray[2]: {}'.format(someArray[2]))

print('the attribute shape of someArray is (call someArray.shape): {}'.format(someArray.shape))

d = [1, 2, 3]
B = [[4, 5, 6],[7, 8, 9]]


np.append(a, B)
#np.append(a, B, axis=1) -> IndexErro: axis 1 out of bounds [0, 1)
np.concatenate(([d], B), axis=0)

#np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], axis=0)


# convert a tuple to an array
t = (1,2,3)
tarr = np.array(t)
type(tarr)
type(tarr[0])

tarr_f32 = np.float32(t)
type(tarr_f32)
type(tarr_f32[0])
