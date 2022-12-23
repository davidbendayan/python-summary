#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 11:38:41 2022

@author: David Bendayan
"""

import numpy as np

# Python Summary

# Variable Assignment

x = 4
y = "Hello"
a, b = 4, 5

# nice for swapping variables easily

a, b = b, a

# Logical operations: and, or, not

# If statement: condition followed by colon, indentation means this is the scope

x, y = 3, 4
if a == 5 or b == 3:
    x = x + 1
    y = y + 2


# Indentation

# newline ends line of code
# \ is used to go to the next line prematurely - it idents automatically
# {} cannot be used
# : is used to start a new block

# Comments

# start using "#" rest of the line is ignored
# """ can include documentation string as the first line of a new function or class you define - dev tools use it and is a good style
def fact(n):
    """


    Parameters
    ----------
    n : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

# For loops:

for count in [5, 7, "hi", 3, 4]:
    print(count)

# While loops:

count = 0
while count < 5:
    print(count)
    count += 1

# Basic Datatypes - Integers, Floats, Strings

# Integer

z = 5 / 2  # Answer 2.5, regular division
z = 5 // 2  # Answer 2, integer division

# Floats

z = 3.456

# Strings
# Strings are Immutable meaning you cannot delete or update a character in a string once it's created. You can use del keyword to delete the
# entire string

String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
String1 = "I'm a Geek"
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
String1 = '''Geeks
            For
            Life'''

# Accessing specific character in string
# Indexer starts from 0.
# Indexer can also start from the end: -1, -2, etc.

String1 = "GeeksForGeeks"
print("\nFirst character of String is: ")
print(String1[0])
print("\nLast character of String is: ")
print(String1[-1])

# String slicing: Use the slicing operator (colon)
# The range given starts from the given index and ends not including the last index

String1 = "Hello"
# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String1[1:3])

# Updating a char in a string - not allowed
String1 = "Hello, I'm a Geek"
String1[2] = 'p'

# Updating entire string - allowed
String1 = "Hello, I'm a Geek"
String1 = "Welcome to the Geek World"

# Deletion of a character - not allowed
String1 = "Hello, I'm a Geek"
del String1[2]

# Deleting entire string - allowed
String1 = "Hello, I'm a Geek"
del String1

# String formatting
# Strings in Python can be formatted with the use of format()

# Default order

String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print String in default order: ")
print(String1)

# Positional Formatting

String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting

String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
print("\nPrint String in order of Keywords: ")
print(String1)

# Formatting of Integers

String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)

# Formatting of Floats

String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

# Rounding off Integers

String1 = "{0:.2f}".format(1 / 6)
print("\one-sixth is : ")
print(String1)

# Naming rules
# Names are case sensitive and cannot start with numbers. They can contain letters, numbers and underscores
# Reserved Words: and, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while
# joined_lower - functions, methods, attributes
# joined_lower or ALL_CAPS - constants
# StudlyCaps - classes
# camelCase - only to conform to pre-existing conventions
# PEP8 convention recommendation guide: https://peps.python.org/pep-0008/

# Sequence Types: Tuples, Lists, Strings

# Tuples: ('john', 32, [CMSC]) - Immutable, Ordered - Simple, Immutable, Ordered sequence of items. Items can be of mixed type, including collection types

# Strings: "John Smith" - Immutable, Ordered conceptually very much like a tuple

# List: [1, 2, 'john', ('up', 'down')] - Mutable, Ordered - ordered sequence of items of mixed types

# Sets: {'foo', 'bar', 'baz'} - Mutable, Unordered - elements are unique, a set itself may be modified , but the elements contained in the set must be of immutable type

# All three sequence types share much the same syntax and functionality

# Key difference: Tuples, Strings are immutable. Lists are mutable.

# Definition of Tuples, Strings, Lists:

tu = (23, ‘abc’, 4.56, (2, 3), ‘def’)


st = “Hello World”
li = [“abc”, 34, 4.34, 23]

# Access individual members of a tuple, string, lists

tu = (23, ‘abc’, 4.56, (2, 3), ‘def ’)


tu[1]  # Second item in the tuple

# Positive and negative indices

t = (23, ‘abc’, 4.56, (2, 3), ‘def ’)


# Positive index: count from the left, starting with 0
t[1]

# Negative index: count from right, starting with –1
t[-3]

#  Slicing: return copy of a subset

t = (23, "abc", 4.56, (2, 3), "def")
t[:2]

# Return a copy of the container with a subset of the original members. Start copying at the first index, and stop copying before second

t[1:4]

# Negative indices count from end

t[1:-1]

# Omit first index to make copy starting from beginning of the container

t[:2]

# Omit second index to make copy starting at first index and going to end

t[2:]

# Copying the Whole Sequence

t[:]

# Important: Note the difference between these two lines for mutable sequences

l2 = l1  # Both refer to 1 ref, changing one affects both
l2 = l1[:]  # Independent copies, two refs

# The ‘in’ Operator

# Boolean test whether a value is inside a container

t = [1, 2, 4, 5]
3 in t

# For strings, boolean check for substring in string

a = 'abcde'
    'cd' in a

    # The + Operator - Produces a new tuple, list, or string whose value is the concatenation of its arguments

    # Tuples

    (1, 2, 3) + (4, 5, 6)
    (1, 2, 3, 4, 5, 6)

        # Lists

    [1, 2, 3] + [4, 5, 6]
    [1, 2, 3, 4, 5, 6]

# Strings

“Hello” + “ ” + “World”

# The * Operator - Produces a new tuple, list, or string that “repeats” the original content

# Tuples

(1, 2, 3) * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)

    # Lists

[1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]

# Strings

“Hello” *3
‘HelloHelloHello’

# Lists are mutable

li = [‘abc’, 23, 4.34, 23]
li[1] = 45
[‘abc’, 45, 4.34, 23]

# We can change lists in place
# Name li still points to the same memory reference when we’re done

# Tuples are immutable

t = (23, ‘abc’, 4.56, (2, 3), ‘def ’)


t[2] = 3.14

# You can’t change a tuple
# You can make a fresh tuple and assign its reference to a previously used name

t = (23, ‘abc’, 3.14, (2, 3), ‘def ’)


# The immutability of tuples means they’re faster than lists

# Operations on Lists Only

li = [1, 11, 3, 4, 5]
li.append(‘a’)
[1, 11, 3, 4, 5, ‘a’]

li.insert(2, ‘i’)
[1, 11, ‘i’, 3, 4, 5, ‘a’]

# The extend method vs +
# + creates a fresh list with a new memory ref
# extend operates on list li in place

li.extend([9, 8, 7])
[1, 2, ‘i’, 3, 4, 5, ‘a’, 9, 8, 7]

# extend takes a list as an argument
# append takes a singleton (one item) as an argument and modifies in place, whereas extend can add multiple items to the list in place

# Operations on Lists Only

li = [‘a’, ‘b’, ‘c’, ‘b’]
li.index(‘b’)  # index of 1st occurrence
li.count(‘b’)  # number of occurrences
li.remove(‘b’)  # remove 1st occurrence
li.reverse()  # reverse the list *in place*
li.sort()  # sort the list *in place*

# The comma is the tuple creation operator

(1, )

# Empty tuples have a special syntactic form

tuple()

# Tuples vs Lists

# Lists slower but more powerful than tuples
# Lists can be modified, and they have lots of handy operations and methods
# Tuples are immutable and have fewer features
# To convert between tuples and lists use the list() and tuple() functions

li = list(tu)
tu = tuple(li)

# Dictionaries - Dictionaries are key and value pairs
# Allows you to identify values by a descriptive name instead of order in a list
# Keys are unordered
# Keys are unique:

my_dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(my_dict['Name']) = > Zara
print(my_dict['Age']) = > 7

my_dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
my_dict['Age'] = 8  # update existing entry
print(my_dict[‘Age’]) = > 8
del dict['Name']  # remove entry with key 'Name'
print(my_dict[“name”]) = > TypeError: Key
Error

# More than one entry per key are not allowed

my_dict = {'Name': 'Zara', 'Age': 7}
print(my_dict['Name']) = > Zara

# Keys must be immutable

my_dict = {['Name']: 'Zara', 'Age': 7}
print(my_dict[‘Name’]) = > TypeError: unhashable
type: 'list'

# Keys can be printed via: my_dict.keys()
# Values can be printed via: my_dict.values()

# popitem() method removes the item that was last inserted into the dictionary

dictionary.popitem()

# pop() method is used to return and delete the value of the key specified

pop_ele = Dict.pop(1)

# clear() - all the items from a dictionary can be deleted at once by using clear() method

Dict.clear()

# del() - deletion of keys can be done by using the del keyword

# Deleting a Key value
del Dict[6]

# Adding elements to the dictionary

Dict = {}
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1

# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4

# Updating existing Key's Value
Dict[2] = 'Welcome'

# Adding Nested Key value to Dictionary
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}

# Accessing elements from a Dictionary

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print(Dict['name'])
# accessing a element using key
print("Accessing a element using key:")
print(Dict[1])

# accessing a element using get()
# method

print("Accessing a element using get:")
print(Dict.get(3))

# Accessing an element of a nested dictionary

Dict = {'Dict1': {1: 'Geeks'},
'Dict2': {'Name': 'For'}}
# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])

# Sets - Unordered, elements are unique, a set itself may be modified, but the elements contained in the set must be of immutable type

# Decalring a set can be done in two ways:

x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
print(x)
{'qux', 'foo', 'bar', 'baz'}

x = {'foo', 'bar', 'baz', 'foo', 'qux'}
print(x)
{'qux', 'foo', 'bar', 'baz'}

# print function needs a parenthesis

print(4)

# range function

# If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions
for i in range(5):
    print(i)

# Important: The given end point is never part of the generated sequence.
list(range(5, 10))
# [5, 6, 7, 8, 9]

# Start is inclusive. End is exclusive.

list(range(0, 10, 3))
# [0, 3, 6, 9]

list(range(-10, -100, -30))
# [-10, -40, -70]

# To iterate over the indices of a sequence, you can combine range() and len() as follows
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t.
# It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.
# We say such an object is iterable, that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted.
# We have seen that the for statement is such a construct, while an example of a function that takes an iterable is sum():

sum(range(4))  # 0 + 1 + 2 + 3

# Numpy Summary

# Basic creation of array elements
a = np.array([1, 2, 3, 4])
print(a)
b = np.ones([4, 4])
print(b)
c = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(c)
print(c.shape)
print(c.dtype)

# Auto creation of array elements - numpy.arange (start, end, step), numpy.linspace (start, end, number of elements), numpy.logspace
# Important: arange = inclusive lower bound, excluding upper bound
a = np.arange(1, 10, 1)
print(a)
b = np.linspace(1, 10, 10)
print(b)
# Important: linspace = inclusive lower bound, inclusive upper bound
c = np.logspace(0, 10, 10, base=numpy.e)
print(c)
# Important: logspace = inclusive lower bound, inclusive upper bound
















