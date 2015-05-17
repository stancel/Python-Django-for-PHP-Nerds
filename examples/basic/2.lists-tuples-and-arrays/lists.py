# Lists are just like PHP's indexed arrays
breakfast = ["eggs", "spam", "bacon", "pancakes", "oatmeal", "yogurt", "toast"]

# You can get elements from a Python list just like you did in PHP
breakfast[0]  # eggs
breakfast[2]  # bacon

# But lists in Python are *much* more featureful.  For example, using our
# breakfast list above:

breakfast[-1]              # toast
breakfast[2:5]             # ["bacon", "pancakes", "oatmeal"]
breakfast[-2:]             # ["yogurt", "toast"]
breakfast.append("juice")  # Adds "juice" to the breakfast list
breakfast.pop()            # Returns "juice", modifying breakfast

# You can even concatenate lists

united_kingdom = ["England", "Wales"] + ["Scotland", "Northern Ireland"]
# Returns: ["England", "Wales", "Scotland", "Northern Ireland"]
