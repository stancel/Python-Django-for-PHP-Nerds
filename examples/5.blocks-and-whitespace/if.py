#!/usr/bin/env python

#
# Python has a hate-on for braces and parentheses unless they're absolutely
# necessary.  Note also that we use `elif` here instead of PHP's `elseif`:
#

if 7 + 3 == 10:
    print("Yes khaleesi, it is known.")

myvar = False
if myvar is True:
    print("It's true!")
elif myvar == 7:
    print("It's seven")
else:
    print("It's false")
