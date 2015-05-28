#!/usr/bin/env python

import sys

#
# Check the length of the argv array to make sure it has the number of arguments
# we want.
#
if not len(sys.argv) == 4:
    print("Usage: 2.calculator.py <number> <operator> <number>")
    sys.exit(1)

#
# The following is equivalent to:
#
# number1 = sys.argv[1]
# operator = sys.argv[2]
# number2 = sys.argv[3]
#
# The use of the __ is a Python standard way of saying "assign output to this
# variable I don't care about"
#
__, number1, operator, number2 = sys.argv

# Make sure the operator is something we can work with
if operator not in ("+", "-", "x", "/"):
    print("We only do simple math today: +, -, x, /")
    sys.exit(1)

#
# Cast the numbers as floats so the math won't explode.  We also need to wrap
# this in a try/except, since float("I am a string") will fail with a
# ValueError:
#
try:
    number1 = float(number1)
    number2 = float(number2)
except ValueError:
    print("We're only doing math on numbers")
    sys.exit(1)

# Python doesn't do switch statements, so if/elif/else is what we do here.
if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "x":
    print(number1 * number2)
else:
    print(round(number1 / number2, 2))
