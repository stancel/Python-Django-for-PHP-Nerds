<?php

    /*
     *
     * In PHP, the concept of drawing other code into your code implies polluting
     * the namespace.  Using require() to load another file into your program
     * necessarily fills your program with the values in that file, potentially
     * overwriting variables and other unpredictable things.
     *
     * In PHP-land, this is mitigated by coding standards and good practise.
     *
     */

    $favourite_colour = "green";
    print("My favourite colour is {$favourite_colour}\n");

    require("variables.php");  // Injects whatever is in variables.php

    print("My favourite colour is {$favourite_colour}\n");

?>
