<?php

    /*
     *
     * PHP re-uses the array() function to create a referenced array.  In fact,
     * PHP's been known to do strange things when you create a referenced array
     * using numeric keys.
     *
     */
    $countries = array(
        "Paris" => "France",
        "Athens" => "Greece",
        "Warsaw" => "Poland",
    );

    print $countries["Athens"];  // Greece

    array_keys($countries);  // array("Paris", "Athens", "Warsaw")

    $countries["Rome"] = "Italy"  // Adds a pairing to the referenced array

?>
