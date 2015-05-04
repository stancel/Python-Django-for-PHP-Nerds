<?php

    // Your typical starting point
    print "Hello World\n";

    // Concatenation
    print "Hello ". "World\n";

    // PHP does simple math just like you'd expect
    print 7 * 5  // 35
    print 2 / 3  // 0.66666666666667

    // It also does its best to figure out what you wanted to do
    print "7" * 5  // 35

    // PHP doesn't have any special syntax for multi-line strings:
    print "
        This is my multi-line string.  Like any other string in PHP, we need
        to be careful with \"quotes\" to be sure to escape them.  Of course,
        you could always use single-quotes (') instead, but then you'd have to
        escape all contractions like the one I just used.
    ";

    // Finally, PHP treats single-quoted strings differently from double-
    // quoted ones:

    $favourite_colour = "green";
    print "My favourite colour is {$green}";  // Variable is interpolated
    print 'My favourite colour is {$green}';  // Not so much

?>
