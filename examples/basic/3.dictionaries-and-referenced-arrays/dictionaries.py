#
# Python dictionaries look a lot like PHP referenced arrays, but you can do
# some crazy things with them.  It's important to note, that unlike PHP,
# dictionaries are simply a key/value store and *not* ordered, for that, you
# should look into using OrderedDict: https://docs.python.org/2/library/collections.html?#collections.OrderedDict
#

countries = {
  "Paris": "France",
  "Athens": "Greece",
  "Warsaw": "Poland",
}

print countries["Athens"]  # Greece

countries.keys()  # Returns a list of capital cities

#
# As there's no restrictions on what you might use as a dictionary key, Python
# lets you do some crazy stuff with dictionaries.  You can use a list as a key,
# or even a dictionary:
#
countries = {
  "Paris": "France",
  "Athens": "Greece",
  "Warsaw": "Poland",
  {
      "provincial": "Amsterdam",
      "national": "Den Haag"
  }: "Netherlands",
}

# Mixing and matching like this is generally bad form though, since you make it
# difficult to predict what's going to be in that dictionary.  It's quite
# reasonable however to define a dictionary with all of its keys being lists.
