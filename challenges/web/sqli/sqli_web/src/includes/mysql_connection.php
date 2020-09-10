<?php
function getConnection($num_challenge) {
	$CREDS = [
		[$_ENV['CHALLENGE0_USER'], $_ENV['CHALLENGE0_USER_PASS']],
		[$_ENV['CHALLENGE1_USER'], $_ENV['CHALLENGE1_USER_PASS']],
		[$_ENV['CHALLENGE2_USER'], $_ENV['CHALLENGE2_USER_PASS']],
		[$_ENV['CHALLENGE3_USER'], $_ENV['CHALLENGE3_USER_PASS']],
	];
	$mysqli = new mysqli($_ENV['DB_HOST'], $CREDS[$num_challenge][0], $CREDS[$num_challenge][1], $_ENV['MYSQL_DATABASE']);
	if ($mysqli->connect_errno) {
		echo "Errno: " . $mysqli->connect_errno . "\n";
		echo "Error: " . $mysqli->connect_error . "\n";
		die();
	}
	return $mysqli;
}
?>
