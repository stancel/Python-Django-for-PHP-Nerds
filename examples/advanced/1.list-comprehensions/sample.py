#
# List comprehensions are an advanced topic, so we don't want to go into it too
# much here, but basically it's a simple way to strip out what you need from
# one list and dump it out into a new one.
#

# Say you have a list like this:

countries = [
    "Canada", "Netherlands", "Greece", "Romania", "Korea", "Australia",
    "Columbia", "Vietnam", "Egypt", "South Sudan", "Mexico"
]

# If you wanted a list of the first letter of each of those, you might do this:

first_letters = []
for country in countries:
    first_letters.append(country[0])

# But you could have just as easily done this:

first_letters = [country[0] for country in countries]

#
# List comprehensions are *very* powerful and allow for all manner of bad ideas,
# including nesting and multiple tests.  You can get a list of countries ending
# in the letter "a" for example:
#

ending_in_a = [country for country in countries if country.endswith("a")]

#
# This isn't so bad, but you probably have a pretty good idea how this can get
# too complicated to read.  The general rule is that if you need this to span
# multiple lines, it's too long and should probably be refactored as a standard
# for loop
#
