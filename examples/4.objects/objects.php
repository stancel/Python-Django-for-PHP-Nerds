<?php

    /*
     *
     * From the start, PHP didn't support objects, and it was instead bolted-on
     * in a later version. The style if follows is reminiscent of Java, sort of:
     *
     */

    class Cake {

        public $flavour;
        public $icing;
        private $temperature;

        function __construct($flavour, $icing) {
            $this->flavour = $flavour;
            $this->icing = $icing;
            $this->temperature = 22;
        }

        public function bake(){
            while ($this->temperature < 180) {
                $this->temperature++;
            }
            return "Baked at ". $this->temperature ."C\n";
        }

    }

    $cake = new Cake("chocolate", "chocolate");
    print($cake->bake());

?>
