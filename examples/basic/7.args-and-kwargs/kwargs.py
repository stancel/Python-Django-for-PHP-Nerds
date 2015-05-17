#
# Python can accept two types of arguments to a method or function, an "arg"
# (argument) or "kwarg" (keyword argument).  Both allow for specific and generic
# uses:
#

#
# Keyword arguments are handy because they allow for a default value.  Calling
# this function without any other arguments would assume the values of "perl",
# "php", and "python" for the first, second, and third arguments.  However, you
# can override those defaults simply by stating them in the call.
#
def my_explicit_kwarg_function(first="Perl", second="PHP", third="Python"):
    print("These were the languages I learnt: {}, {}, {}".format(
        first,
        second,
        third
    ))

# You could call this function, replacing the first argument with "C#" for
# example:
my_explicit_kwarg_function(first="C#")

# Or you could override them all:
my_explicit_kwarg_function(first="R", second="C++", third="Erlang")

# Or just the third:
my_explicit_kwarg_function(third="Erlang")

#
# Just like *args, keyword arguments have a generic form as well.  You can use
# **kwargs to say "Whatever keyword arguments were passed in", and it will be
# available to the function as a dictionary:
#
def my_generic_kwarg_function(**kwargs):
    for key, value in kwargs.items():
        print("This key/value pair was passed into this function: {}/{}".format(
            key,
            value
        ))

# So this method can be called with as many keyword arguments as you like:
my_generic_kwarg_function(
    first="C",
    second="C++",
    third="Haskel",
    fourth="Portugese",
    favourite="Python",
)

# Note that you cal also pass arguments with **.  The code below passes the 3
# keyword argument in my_dict as separate keyword arguments:

my_dict = {"first": "C", "second": "PHP", "third": "Python"}
my_explicit_kwarg_function(**my_dict)

#
# Calling functions with keyword arguments is *very* common in Python and
# especially common in Django, so it's best to get used to them.
#
