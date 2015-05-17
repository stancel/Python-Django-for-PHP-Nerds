<?php

  /*
   *
   * Exception handling in PHP is incomplete, and typically restricted to user
   * space.  That is to say, when you try to do something that just won't work
   * in PHP, your code will just fail (sometimes silently) but this is not
   * considered an exception.  Instead, you need to test for something and throw
   * your own exception.
   *
   * The following is from the PHP docs:
   *
   */

  function inverse($x) {
      if (!$x) {
          throw new Exception('Division by zero.');
      }
      return 1/$x;
  }

  try {
      echo inverse(5) . "\n";
  } catch (Exception $e) {
      echo 'Caught exception: ',  $e->getMessage(), "\n";
  } finally {
      echo "First finally.\n";
  }

  try {
      echo inverse(0) . "\n";
  } catch (Exception $e) {
      echo 'Caught exception: ',  $e->getMessage(), "\n";
  } finally {
      echo "Second finally.\n";
  }

  // Continue execution
  echo "Hello World\n";

?>
