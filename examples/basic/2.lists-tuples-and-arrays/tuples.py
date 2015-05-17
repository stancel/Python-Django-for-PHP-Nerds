# Lists are just like PHP's indexed arrays
breakfast = ("eggs", "spam", "bacon", "pancakes", "oatmeal", "yogurt", "toast")

# You can get elements from a Python list just like you did in PHP
breakfast[0]  # eggs
breakfast[2]  # bacon

# But lists in Python are *much* more featureful.  For example, using our
# breakfast list above:

breakfast[-1]              # toast
breakfast[2:5]             # ["bacon", "pancakes", "oatmeal"]
breakfast[-2:]             # ["yogurt", "toast"]

# But tuples are immutable, meaning you can't modify them:

breakfast.append("juice")  # Exception!
breakfast.pop()            # Exception!

# If you need to modify them however, you can re-cast them as a list:

modified_breakfast = list(breakfast)
modified_breakfast.append("juice")

