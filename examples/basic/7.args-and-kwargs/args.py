#
# Python can accept two types of arguments to a method or function, an "arg"
# (argument) or "kwarg" (keyword argument).  Both allow for specific and generic
# uses:
#

#
# This is probably what you're used to.  If a function had 3 arguments, and you
# must pass in all three for the function to work
#
def my_explicit_arg_function(first, second, third):
    print("These are my arguments: {}, {}, {}".format(
        first,
        second,
        third
    ))

# You would call this function like this:
my_explicit_arg_function("cake", "pizza", "ice cream")


#
# Python allows for a more open-ended notation for arguments.  The use of *args
# basically says: "all arguments passed to this function" and represents these
# arguments as a list.
#
def my_generic_arg_function(*args):
    for argument in args:
        print("This was an argument".format(argument))

# You could call this function just like the last one, but you can use as many
# or as few arguments as you like:

# You would call this function like this:
my_generic_arg_function("cake", "pizza", "ice cream", "doughnuts")
my_generic_arg_function("cake")

# Note that you can also pass arguments with *.  The code below passes the 3
# arguments in my_list as separate arguments:

my_list = ["cake", "pizza", "ice cream"]
my_explicit_arg_function(*my_list)
