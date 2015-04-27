#!/usr/bin/env python

#
# Python supports exceptions at the core of the language.  If something happens
# that doesn't make sense, Python will explode with an exception rather than
# continue with unpredictable behaviour.
#
# These exceptions are specifically named too, so you can listen for a
# particular type and do different things based on which type of exception was
# raised.
#

def inverse(x):
    """
    Math in Python is less liberal about types.  See the example files titled
    "Section 1: Strings, Integers, and Floats"
    """
    return 1.0 / float(x)

try:
    print(inverse(5))
except ZeroDivisionError as e:
    print("Caught exception: {}".format(e))
finally:
    print("First finally")

try:
    print(inverse(0))
except ZeroDivisionError as e:
    print("Caught exception: {}".format(e))
finally:
    print("Second finally")

# Continue execution
print("Hello World")

#
# As I said above, Python's exception handling is a lot more powerful that what
# you might be used to in PHP.  You can make use of standard exceptions like
# ZeroDivisionError, IndexError, or ValueError, or create your own exceptions
# for whatever purpose you like.
#

# Our "database" of Starfleet captains
my_list = {
    "janeway": "Voyager",
    "sisko": "Deep Space Nine",
    "picard": "The Next Generation",
    "kirk": "The Original Series",
    "archer": "Enterprise"
}

# Create our own custom exception
class TerribleChoiceException(Exception):
    pass

# Here's our code that will print a message
def favourite_captain(name):
    if name == "archer":
        raise TerribleChoiceException()
    return "{} was the captain on {}".format(name, my_list[name])

# Here, if we set my_choice to "janeway", we'll get "Janeway was the captain on
# Voyager".  If we set it to "Cousteau", it will complain that we're not talking
# about the same show, and if you select "Archer", it will school you in your
# preference for Starfleet captains.

try:
    print(favourite_captain(my_choice))
except TerribleChoiceException:
    print("No, I won't accept Archer as a favourite Starfleet captain.")
except KeyError:
    print("I'm not sure that we're talking about the same show.")
