<?php

// WRITE the credentials OF the Postgres DATABASE.
date_default_timezone_set('America/Los_Angeles');

$hostname = "ec2-54-229-68-88.eu-west-1.compute.amazonaws.com";
$dbname = "dac8mdcg8q30i6";
$username = "camkqjlqrcturt";
$pass = "26a6b969df31e3a6e2e4d0d7074f4b77345d6f972d6d5ad1910d887c03847db2";

// CREATE the connection TO the PostgreSQL
$conn = pg_connect(" host = $hostname dbname = $dbname user = $username password = $pass ");

if($conn){

if($_SERVER['REQUEST_METHOD']=='POST'){
	$data = file_get_contents('php://input');
	$time = time();

	$query1 = "INSERT INTO Info  (Requests, Timestamp) VALUES ('$data','$time')";
	$result = pg_query($conn, $query1 );
		
}
}

else{
	echo "Failed to connect";
}
?>