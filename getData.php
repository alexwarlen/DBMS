<?php 
    $con = mysqli_connect('egr4.campus.up.edu','warlen17','warlen17','warlen17')
    or die('Error connecting to MySQL server.');
    // This is just an example of reading server side data and sending it to the client.
    // It reads a json formatted text file and outputs it.

    
    echo "hello world...";
    
    /*$query = "Select * from test";
    echo $query;
    
    $exec = mysqli_query($con,$query);
    echo $exec;*/

// Instead you can query your database and parse into JSON etc etc

?>