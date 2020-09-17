<?php
$SQL_QUERY = "SELECT id,flag FROM challenge2 WHERE id='%s';";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
	$flag_id = $_POST["flagID"];
	if (isset($flag_id)) {

		include("mysql_connection.php");
		$mysqli = getConnection(2);
		if ($mysqli->connect_errno) {
			echo "Errno: " . $mysqli->connect_errno . "\n";
			echo "Error: " . $mysqli->connect_error . "\n";
			die();
		}
		$QUERY_STRING = sprintf($SQL_QUERY, $flag_id);
		$query = $mysqli->query($QUERY_STRING);
		if (strlen($mysqli->error) > 0) {
			$ERROR = $mysqli->error;
		}
		if($query) {
			$query->close();
		}
		$mysqli->close();
	} else {
		$ERROR = "Veuillez entrer un id à chercher.";
	}
}
?>
