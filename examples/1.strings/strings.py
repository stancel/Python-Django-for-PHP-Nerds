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

# Remember that you Python doesn't think for you when you try to mix strings and
# non-strings.  For example, this will explode with a TypeError exception:

print("Hello Agent 00" + 7)

# Instead, you should be either casting that 7 as a string with str(), or using
# .format()

print("Hello Agent 00" + str(7))
print("Hello Agent {}".format(7))

# The use of .format() leads to the topic of advanced string formatting.  It's
# beyond the scope of this tutorial, but if you're curious:

# https://docs.python.org/2/library/string.html#format-specification-mini-language
print("Hello Agent {number:03d}".format(number=7))
