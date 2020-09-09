<?php
$SQL_QUERY = "SELECT * FROM challenge1 WHERE id='%s';";
$ROW_FORMAT = '<tr><td>%d</td><td>%s</td><td>%s</td><td>%s</td>/tr>';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
	$msg_id = $_POST["msgID"];
	if (isset($msg_id)) {

		include("mysql_connection.php");
		$mysqli = getConnection(1);
		if ($mysqli->connect_errno) {
			echo "Errno: " . $mysqli->connect_errno . "\n";
			echo "Error: " . $mysqli->connect_error . "\n";
			die();
		}
		$QUERY_STRING = sprintf($SQL_QUERY, $msg_id);
		$query = $mysqli->query($QUERY_STRING);
		if (strlen($mysqli->error) > 0) {
			$ERROR = $mysqli->error;
		}
		if($query) {
			$RESULT = $query->fetch_all();
			$query->close();
		}
		$mysqli->close();
	} else {
		$ERROR = "Veuillez entrer un id à chercher.";
	}
}
?>
