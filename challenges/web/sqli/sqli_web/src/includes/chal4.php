<?php
$SQL_QUERY = "SELECT id,flag FROM challenge4 WHERE id='%s';";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
	$flag_id = $_POST["flagID"];
	if (isset($flag_id)) {

		include("mysql_connection.php");
		$mysqli = getConnection(4);
		if ($mysqli->connect_errno) {
			echo "Errno: " . $mysqli->connect_errno . "\n";
			echo "Error: " . $mysqli->connect_error . "\n";
			die();
		}
		$ERROR = False;
		$QUERY_STRING = sprintf($SQL_QUERY, $flag_id);
		$query = $mysqli->query($QUERY_STRING);
		if($query) {
			$query->close();
		}
		$mysqli->close();
	}
}
?>
