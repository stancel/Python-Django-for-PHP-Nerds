#!/usr/bin/env python

# We need the sys module, because it has access to the arguments list (argv)
import sys


# See below why we're wrapping everything in a function rather than just laying
# out our business logic from the start.
def do_hello():
    # Test the length of the list to make sure there's at lest 2 arguments. Just
    # like in PHP, 0 is the name of the script being executed.
    if len(sys.argv) > 1:
        # You access the argument we want with [1] and concatenate it to the
        # "Hello " string, passing all of this to print().  A "\n" is implied.
        print("Hello " + sys.argv[1])
    else:
        print("Usage: python 1.hello.py <name>")

#
# If you import a python file, it will execute the code inside it, which isn't
# always preferable.  Typically, it's a good habit to get into wrap your script
# logic (no matter how simple) in a function with `def` and then use this little
# if block to execute it only if the script is executed deliberately.
#
# For the other more complex examples, we won't be doing this, just to keep
# things more on-topic, but this is a pattern best followed in your own work.
#
if __name__ == "__main__":
    do_hello()

#
# For people comfortable with exceptions, this could also be accomplished with
# a try/except checking for an IndexError.
#
