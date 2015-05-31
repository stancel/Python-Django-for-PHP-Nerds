#!/usr/bin/env python

# We need the random module to make an easy selection, and sys to get arguments.
import random
import sys

# Here's our "database": a dictionary of dictionaries of lists.
people = {
    "Marshall": {
        "pronoun": "he",
        "foods": ["Beer", "Olives", "Pizza"]
    },
    "Lilly": {
        "pronoun": "she",
        "foods": ["Marshmallows", "Olives", "Cheese", "Gin & Tonic"]
    },
    "Ted": {
        "pronoun": "he",
        "foods": ["Croissants", "Bagels", "Beer"]
    },
    "Barney": {
        "pronoun": "he",
        "foods": ["Wine", "Beer"]
    },
    "Robin": {
        "pronoun": "she",
        "foods": ["Wine", "Cheese"]
    },
}


# This is the simplest way to generate the message, and probably the cleanest.
# We're using Python's .format() minilanguage here, and the .join() method
# available to all strings.  Basically, .format() is like sprintf() on crack,
# and we're using it to substitute the {} for our variables.  In the case of
# .join, think of it as the same as implode():
# http://php.net/manual/en/function.implode.php
def get_message(person):
    return "Ah yes {}, {} likes:\n  * {}".format(
        person,
        people[person]["pronoun"],
        "\n  * ".join(people[person]["foods"])
    )


# The alternative here isn't used, but I've included it in case the other
# function doesn't make sense.  This is a much more PHP-way of doing things:
# build a string with a for loop.  Both ways are totally normal in Python, but
# I find the other function less messy and more readable.
def alternate_get_message(person):

    pronoun = people[person]["pronoun"]

    message = "Ah yes " + person + ", " + pronoun + " likes:\n"

    for food in people[person]["foods"]:
        message += "  * " + food + "\n"

    # .strip() strips off excess whitespace, like the extra \n applied in the
    # loop.
    return message.strip()


# .keys() returns all of the keys from a dictionary
acceptable_people = list(people.keys())  # Python3 returns dict_keys here, rather than a plain list.

if not len(sys.argv) == 2:
    # For our random selection, we use random.choice() which returns a random
    # element from a list, and then we pass that element (one of the names) to
    # get_message()
    print(get_message(random.choice(acceptable_people)))

# We can test if the user has passed an acceptable name with the "in" operator
elif sys.argv[1] in acceptable_people:
    print(get_message(sys.argv[1]))

else:
    print("Sorry, I have no idea who that is.")
    sys.exit(1)
