<?php
$database_host = "dbhost.cs.man.ac.uk";
$database_user = "h54023kc";
$database_pass = "y20-pass";
$group_dbnames = "2021_comp10120_y20";

$conn = mysqli_connect($database_host,$database_user,$database_pass,$group_dbnames);

/* 
User TABLE  
(UserID int -primary key auto_increment
Email varchar
password-varchar)



Liked TABLE 
(Likeid int primary key auto_increment
Disliked bit
Userid int - foreignkey
Restaurantid int -foreignkey
)

*/




//sql for Liked Restaurant
$sql = Insert into Liked (UserID, RestaurantID, Disliked) values(variable1, variable2, 0)

//sql for Disliked Restaurant
$sql1 = Insert into Liked (UserID, RestaurantID, Disliked) values(variable1, variable2, 1)

//sql to select all restaurants liked by a user
$sql2 = SELECT Distinct RestaurantID FROM Liked WHERE UserID = ‘variable’ AND Disliked = 0

//sql to select all Users that like a restaurant
$sql3 = SELECT Distinct UserId FROM Liked WHERE RestaurantID = ‘variable’ AND Disliked = 0

// sql to select all restaurants that the user hasn’t swiped
$sql4 = SELECT Distinct * FROM Restaurant WHERE RestaurantID NOT IN(SELECT Distinct restaurantID FROM Liked WHERE Userid = ‘variable’)


?>
