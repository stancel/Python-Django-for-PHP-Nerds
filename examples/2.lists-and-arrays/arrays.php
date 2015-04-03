<?php

    # PHP arrays are created, like everything else, by way of a function:
    $breakfast = array("eggs", "spam", "bacon", "pancakes", "oatmeal", "yogurt", "toast");

    # But to get properties of that array, you typically operate on the array itself
    $breakfast[0];  # eggs
    $breakfast[2];  # bacon

    # Except when you're doing something more advanced, then you use a
    # function:

    array_slice($breakfast, -1);      # "toast"
    array_slice($breakfast, 2, 3);    # array("bacon", "pancakes", "oatmeal")
    array_slice($breakfast, -2, 2);   # array("yogurt", "toast")
    array_push($breakfast, "juice");  # Adds "juice" to $breakfast
    array_pop($breakfast);            # Returns "juice", removing it from the array

    # If you want to concatenate arrays, you need a function for that too
    $united_kingdom = array_merge(
        array("England", "Wales"),
        array("Scotland", "Northern Ireland")
    );  #  Returns array("England", "Wales", "Scotland", "Northern Ireland")

?>
