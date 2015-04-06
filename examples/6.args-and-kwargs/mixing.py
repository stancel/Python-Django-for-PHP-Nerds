#
# There's no reason to keep *args and **kwargs separate.  More often than not,
# they're used together.  We can illustrate this with a super-common use-case:
#

#
# An __init__ method on an object typically has some defaults that we want to
# allow to be overridden, and others that must be defined.  In this case, we've
# got a User object that requires a `name` parameter, and a default
# `distance_travelled` value of 0:
#
class User(object):
    def __init__(self, name, distance_travelled=0):
        self.name = name
        self.distance_travelled = distance_travelled

# We can instantiate our user with a name and a distanced_travelled value 0 by
# using any of these three methods:
frodo = User("Frodo")
frodo = User("Frodo", 0)
frodo = User("Frodo", distance_travelled=0)

# The thing to remember is that *order matters*.  Keyword arguments must come
# after all of your standard arguments, so this is ok:

def my_working_function(first, second, favourite=None, least_favourite=None):
    pass

# But this is not:

def my_broken_function(first, favourite=None, second, least_favourite=None):
    pass
