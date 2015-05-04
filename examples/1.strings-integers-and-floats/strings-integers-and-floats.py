#
# In Python's print() function, the "\n" is implied.
#

# Your typical starting point
print("Hello World")

# Concatenation
print("Hello " + "World")

# Strings are objects in Python
print("hello".capitalize())  # Prints "Hello"
print("hello".upper())       # Prints "HELLO"
print("HeLLo".lower())       # Prints "hello"
print("hello".center(11))    # Prints "   hello   "

"hello".startswith("h")  # Returns True
"hello".startswith("e")  # Returns False

# They're also indexed
print("hello"[2])    # Prints "l"
print("hello"[-1])   # Prints "o"
print("hello"[-2:])  # Prints "lo"

# Multiline comments make use of the special triple-quote (""") syntax:
print("""This is my multiline string. It's handy for large blocks of text,
because you can use "quotes" in them without worrying about having to escape
anything.""");

# Remember that Python doesn't think for you when you try to mix strings and
# non-strings.  For example, this will explode with a TypeError exception:

print("Hello Agent 00" + 7)

# Instead, you should be either casting that 7 as a string with str(), or using
# .format()

print("Hello Agent 00" + str(7))
print("Hello Agent {}".format(7))

# Since Python doesn't make use of special syntax (like PHP's "$"), there's no
# way to handle interpolated strings in Python.  Instead, we use the .format()
# method.

favourite_colour = "green"
print("My favourite colour is {}".format(green))

# The use of .format() leads to the topic of advanced string formatting.  It's
# beyond the scope of this tutorial, but if you're curious:

# https://docs.python.org/2/library/string.html#format-specification-mini-language
# http://pyformat.info/
print("Hello Agent {number:03d}".format(number=7))

#
# As you saw above, Python is a lot more strict when it comes to object types.
# You can't add a string to an integer or divide a float by a string.  Obviously
# this can be a problem when you've got a string tht you'd like to treat like
# a number, or a number you want to treat like a string, so Python provides
# casting functions to change the nature of your objects.
#

# The result of this might surprise you
print("7" * 3)  # "777" or rather, "the string '7' repeated 3 times"

# Do do some math though, we cast the string as an int
print(int("7") * 3)  # 21

# Same goes if you want to concatenate "3" to the "7":
print("7" + str(3))  # "73"

# You would normally use these functions on variables of course, as one-part
# variable sanitisation and one-part casting for use in your program:

try:
    print(int(argument1) * int(argument2))
except TypeError:
    print("Looks like you didn't actually provide integers.  Try again.")

# You can also test for the type of a variable with type() or isinstance():

type(my_variable)                 # Returns int, str, float, etc.
type(7) == int                    # True
isinstance(7, int)                # True
isinstance(7, (int, str, float))  # True because 7 is one of (int, str, float)

# Lastly, an annoying story about Python 2 vs. 3.

# In Python 2 this returns 1
print(10 / 6)  # 1

# Obviously, we know that's not the case, but Python 2 treats math done on
# integers as integer-only math.  If there's a remainder, you don't get to see
# it.  So rather than 1.6666666666666667, you get just the integer part.  It
# doesn't even bother to round!

# In Python 3, this does what you'd expect:
print(10 / 6)  # 1.6666666666666667

# The solution to this in Python 2 (and probably still good practise in Python
# 3) is to cast your numbers as floats:
print(float(10) / float(6))  # 1.6666666666666667

# It's annoying, but makes a very Pythonic sense.  If you operate on integers,
# you get integers, if you operate on floats, you get floats.
