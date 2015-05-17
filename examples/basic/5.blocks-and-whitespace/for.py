from random import randint

#
# Python's syntax for loops is **much** simpler and more powerful.
#

people = [
    {"name": "Kalle", "salt": 856412},
    {"name": "Pierre", "salt": 215863}
]

# Python operates using references rather than copies of data:
for person in people:
    person["salt"] = randint(0, 999999)
