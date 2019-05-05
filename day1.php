<?php
$handle = fopen ("php://stdin","r");
$i = 4;
$d = 4.0;
$s = "HackerRank ";

// Declare second integer, double, and String variables.
$numero1;
$numero2;
$nombre;

// Read and save an integer, double, and String to your variables.
fscanf($handle, "%d\n", $numero1); // lee un número de STDIN
fscanf($handle, "%d\n", $numero2); // lee un número de STDIN
fscanf($handle, "%s\n", $nombre); // lee un número de STDIN
// Print the sum of both integer variables on a new line.
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
