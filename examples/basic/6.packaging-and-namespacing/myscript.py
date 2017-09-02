#
# In Python, everything is namespaced according to the package it came from.
# As a result, it's simply impossible to overwrite one part of your program with
# another unless you explicitly set the local value to one from another package.
#

# Important note: imports ALWAYS go at the top of the file.  Python will let you
# get away with importing stuff anywhere (even inside a function), but it's
# generally considered bad practice since it makes your program harder to
# understand.
import variables

print(favourite_food)  # Exception!
print(variables.favourite_food)  # "cake"
