#
# Python lets you create x-like objects, as in, you can create an object that
# behaves like a list, or a dictionary, or string, or whatever you like.  This
# is accomplished by taking advantage of the special "double-underscore" methods
# like __init__, __iter__, __str__ etc.
#
# Since all Python lists are just objects that support a standard list-like
# interface, you can create an object that implements that interface.  Then pass
# it around as if it's a typical list.
#
# You see a lot of magic like this in frameworks like Django that want to hide
# complexity from you when you don't need it.  The result of a query is made
# available through a QuerySet object, which is list-like.  You can loop over
# it, or even take the first, second, and third values with square brackets,
# just like a typical list.
#
# Below I've given you a very crude implementation of a list-like object that
# shows you how you might make use of a database (it could be some 3rd-party
# thing or just a CSV file on disk) as a list:
#

class MyListLikeThing(object):

    DATABASES = {
        "europe": ["uk", "fr", "nl", "de", "gr", "it"],
        "americas": ["ca", "us", "mx", "vz", "ci", "co"],
    }

    def __init__(self, db):
        self._db = db  # This could be a anything, like a remote datastore

    def __iter__(self):
        for country in self.DATABASES[self._db]:
            yield country

    def __repr__(self):
        return 'My custom list-like object using the "{}" database backend.'.format(
            self._db
        )

europe = MyListLikeThing("europe")
americas = MyListLikeThing("americas")

print(americas)

for country in americas:
    print("Code: " + country)

print(list(europe))
