# Tutorial: https://www.learnpython.org/en/Variables_and_Types

# Python is completely object oriented, and not "statically typed". You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.

# Numbers
# Python supports two types of numbers - integers and floating point numbers.

# Integer:
myint = 7
print(myint)

# Floating point number
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# Strings
# Strings are defined either with a single quote or a double quotes. (The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes))
mystring = 'Hello '
print(mystring)
mystring = "World!"
print(mystring)

# Simple operators can be executed on numbers and strings:
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# Assignments can be done on more than one variable "simultaneously" on the same line like this:
a, b = 3, 4
print(a,b)

# Mixing operators between numbers and strings is not supported:
# This will not work! (Problem on line 46)
one = 1
two = 2
hello = "hello"

# print(one + two + hello) - Commented out becuase it will mess up the code.

# Exercise
# The target of this exercise is to create a string, an integer, and a floating point number. The string should be named mystring and should contain the word "hello". The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.
# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
    
