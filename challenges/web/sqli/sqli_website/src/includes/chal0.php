<?php
$SQL_QUERY = "SELECT * FROM challenge0 WHERE username='%s';";
$ROW_FORMAT = "<tr><td>%d</td><td>%s</td><td>%s</td></tr>";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
	$username = $_POST["username"];
	$pass = $_POST["password"];
	if (isset($username)) {

		include("mysql_connection.php");
		$mysqli = getConnection(0);
		if ($mysqli->connect_errno) {
			echo "Errno: " . $mysqli->connect_errno . "\n";
			echo "Error: " . $mysqli->connect_error . "\n";
			die();
		}
		$QUERY_STRING = sprintf($SQL_QUERY, $username);
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
		$ERROR = "Veuillez entrer un username à chercher.";
	}
}
?>
