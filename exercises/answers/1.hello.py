#!/usr/bin/env python

# We need the sys module, because it has access to the arguments list (argv)
import sys

# Test the length of the list to make sure there's at lest 2 arguments. Like in
# Perl, 0 is the name of the script being executed.
if len(sys.argv) > 1:
    # You access the argument we want with [1] and concatenate it to the
    # "Hello " string, passing all of this to print().  A "\n" is implied.
    print("Hello " + sys.argv[1])
else:
    print("Usage: python 1.hello.py <name>")

#
# For people comfortable with exceptions, this could also be accomplished with
# a try/except checking for an IndexError.
#
