<!DOCTYPE html>
<?php
  include_once "dbh.inc.php";

?>
<html>
 <head>
   <title>Database Connection Test</title>
 </head>
 <body>
   <form>
   <h1>Test</h1>
   <?php
    $sql = "SELECT * FROM users;";
    $results = mysqli_query($conn, $sql);
    $resultCheck = mysqli_num_rows($results);
    if ($resultCheck > 0){
      while ($row = mysqli_fetch_assoc($results)){
        //echo($row['userID']);
        echo '<pre>'; print_r($row); echo '</pre>';
        echo("<br>");
      }
    }
   ?>
  </form>
 </body>
</html>
