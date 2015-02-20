<?php

    # A "list" is basically a PHP array
    $breakfast = array("eggs", "spam", "bacon", "pancakes", "oatmeal", "yogurt", "toast");

    $breakfast[0];  # eggs
    $breakfast[2];  # bacon

    # But lists in Python are *much* more featureful.  For example, using our
    # breakfast list above:
    
    array_slice($breakfast, -1);     # toast
    array_slice($breakfast, 2, 3);   # array("bacon", "pancakes", "oatmeal")
    array_slice($breakfast, -2, 2);  # array("yogurt", "toast");

?>
