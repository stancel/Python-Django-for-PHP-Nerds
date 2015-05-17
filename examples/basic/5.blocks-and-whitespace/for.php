<?php

    /*
     *
     * This example is stolen right from the PHP website.
     *
     */

    $people = array(
        array('name' => 'Kalle', 'salt' => 856412),
        array('name' => 'Pierre', 'salt' => 215863)
    );

    for($i = 0; $i < count($people); ++$i) {
        $people[$i]['salt'] = mt_rand(000000, 999999);
    }

?>
