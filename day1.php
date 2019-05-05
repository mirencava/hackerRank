<?php
$handle = fopen ("php://stdin","r");
$i = 4;
$d = 4.0;
$s = "HackerRank ";

// Declare second integer, double, and String variables.
$numero1 = 12;
$numero2 = 4.0;
$nombre = "is the best place to learn and practice coding!";

// Print the sum of both integer variables on a new line.
print ($numero1 + $i . "\n");


// Print the sum of the double variables on a new line.
$suma =$numero2 + $d;
print number_format($suma, 1, '.', ',')."\n";
// Concatenate and print the String variables on a new line
// The 's' variable above should be printed first.
print ($s . $nombre . "\n");

fclose($handle);
?>
