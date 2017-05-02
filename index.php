<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="jquery-3.2.0.min.js"></script>
    <!--Load the AJAX API-->
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
	 <script type="text/javascript" src="controller.js"></script>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    
    <meta name="description" content="">
    <meta name="author" content="">
		<style>
		#visualization {
		width: 1000px;
		height: 700px;
		}</style>

    <title>Team Rocket - Database Management Systems</title>
    
    
    
    </head>
        <body > 
            <div>
             <img src="teamrocket.jpg" style="width:152px;height:114px; float:left;">
                <h1 style="margin-left:30px; margin-bottom:15px; color:#CF3721; ">Team Rocket</h1>
           
                </div>
            <div class="container" style="margin-left:20px">                                          
      <div class="dropdown">
        <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown" id="hi" style="background-color:#31A9B8; border:none">Timezones
            <span class="caret"></span>
        </button>
        <ul class="dropdown-menu" id="hi">
          <li><a href="#">Timezones</a></li>
          <li><a href="#">Top Retweets</a></li>
          <li><a href="#">Tweets Over Time</a></li>
        </ul>
      </div>
    </div>
            
<div id="chart_div" style="width:600; height:400; margin-left:30px"></div>
        </body>

</html>



<?php
$servername = "localhost";
$username = "root";
$password = "elvisp";
$dbname = "teamrocket";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
//echo "Connected successfully";

$sql = "SELECT * FROM hashtags";
$result = mysqli_query($conn, $sql);
$var = mysqli_fetch_array($result,MYSQLI_BOTH);
if (mysqli_num_rows($result) > 0) {
    // output data of each row
    while($row = mysqli_fetch_assoc($result)) {
        //echo "tweet_id: " . $row["tweet_id"]. " - user_id: " . $row["user_id"]. " " ."hashtag: " . $row["hashtag"]. "<br>";
    }
} else {
    echo "0 results";
}


?>

<script language="javascript">
        $(".dropdown-menu li a").click(function(){
  $(this).parents(".dropdown").find('.btn').html($(this).text() + ' <span class="caret"></span>');
  $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
});
    // Load the Visualization API and the piechart package.
      google.charts.load('current', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(drawChart);

      // Callback that creates and populates a data table, 
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart() {

      // TIMEZONES //////////
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Timezone');
      data.addColumn('number', 'Count');
      
          
      data.addRows([
        <?php
          $servername = "localhost";
          $username = "root";
          $password = "****";
          $dbname = "teamrocket";

          // Create connection
          $conn = mysqli_connect($servername, $username, $password, $dbname);

          // Check connection
          if ($conn->connect_error) {
              die("Connection failed: " . $conn->connect_error);
          } 
          
          $sql = "SELECT timezone, count(*) as `count` from (select distinct * from `users`) as `tab` where `timezone` != \"\" group by `timezone` order by `count` desc";
          
          $result = mysqli_query($conn, $sql);

          if (mysqli_num_rows($result) > 0) {
                // output data of each row
                $numrows = mysqli_num_rows($result);
                while($row = mysqli_fetch_assoc($result)) {
                    if ($numrows > 1) {
                        echo "[ '" . $row["timezone"]. "', " . $row["count"]. " ],";
                        
                    }
                    else {
                        echo "[ '" . $row["timezone"]. "', " . $row["count"]. " ]";
                    }
                    $numrows = $numrows -1;
                    //echo $numrows;
                }
            }
            else {
               // echo "0 results";
            }


        ?>
      ]);
          
          ///////////////////////// top retweets
          
          var topretweets = new google.visualization.DataTable();
      topretweets.addColumn('string', 'Tweet Text');
      topretweets.addColumn('number', 'Number of Retweets');
      
          
      topretweets.addRows([
        <?php
          $servername = "localhost";
          $username = "root";
          $password = "****";
          $dbname = "teamrocket";

          // Create connection
          $conn = mysqli_connect($servername, $username, $password, $dbname);

          // Check connection
          if ($conn->connect_error) {
              die("Connection failed: " . $conn->connect_error);
          } 
          
          $sql = "select distinct tweets.tweet_text, tweets.retweets from (select  * from tweets) as `tweets` order by cast(tweets.retweets as signed) desc limit 10";
          
          $result = mysqli_query($conn, $sql);
          
          if (mysqli_num_rows($result) > 0) {
                // output data of each row
                $numrows = mysqli_num_rows($result);
                while($row = mysqli_fetch_assoc($result)) {
                    if ($numrows > 1) {
                        echo "[ '" . addslashes($row["tweet_text"]). "', " . $row["retweets"]. " ],";
                        
                    }
                    else {
                        echo "[ '" . addslashes($row["tweet_text"]). "', " . $row["retweets"]. " ]";
                    }
                    $numrows = $numrows -1;
                    //echo $numrows;
                }
            }
            else {
               // echo "0 results";
            }


        ?>
      ]);
          
          
          /////////////////////
          
          /// tweets over time ///
          var tweetsovertime = new google.visualization.DataTable();
      tweetsovertime.addColumn('string', 'Date');
      tweetsovertime.addColumn('number', 'Number of Tweets');
      
          
      tweetsovertime.addRows([
        <?php
          $servername = "localhost";
          $username = "root";
          $password = "****";
          $dbname = "teamrocket";

          // Create connection
          $conn = mysqli_connect($servername, $username, $password, $dbname);

          // Check connection
          if ($conn->connect_error) {
              die("Connection failed: " . $conn->connect_error);
          } 
          
          $sql = "select date_format(created_at, '%Y-%m-%d') as `the_date`, count(*) as `count` from tweets where `created_at` between date_format( '2017-4-1', '%Y-%m-%d') and date_format('2017-4-20', '%Y-%m-%d') group by the_date";
         
        
          $result = mysqli_query($conn, $sql);
            
          if (mysqli_num_rows($result) > 0) {
                // output data of each row
                $numrows = mysqli_num_rows($result);
                while($row = mysqli_fetch_assoc($result)) {
                    if ($numrows > 1) {
                        echo "[ '" . addslashes($row["the_date"]). "', " . $row["count"]. " ],";
                        
                    }
                    else {
                        echo "[ '" . addslashes($row["the_date"]). "', " . $row["count"]. " ]";
                    }
                    $numrows = $numrows -1;
                    //echo $numrows;
                }
            }
            else {
               // echo "0 results";
            }


        ?>
      ]);
          
    
          

      // Set chart options
      var options = {'title':'Timezones of users posting about University of Portland',
                     'width':800,
                     'height':500,
                     'colors':['#F5BE41']
                    };

          var options2 = {'title':'Top Retweeted Tweets',
                     'width':800,
                     'height':600,
                    'colors':['#258039']
                    };
          var options3 = {'title':'Number of Tweets Over Time',
                     'width':1000,
                     'height':600,
                    'colors':['#CF3721']
                    };
      // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
        chart.draw(data, options);
          $(".dropdown-menu li a").click(function(){
        var whichVis = document.getElementById('hi').text;
          var selectedVisualization = $(this).text();
            if (selectedVisualization == "Timezones"){
                var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
        chart.draw(data, options);
            
            }
          else if (selectedVisualization == "Top Retweets"){
                var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
        chart.draw(topretweets, options2);
            }
            else {
                var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
        chart.draw(tweetsovertime, options3);
            }
          });
        
    }
</script>
