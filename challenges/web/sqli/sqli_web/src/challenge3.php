<?php
include("includes/chal3.php");
?>

<html>
<head>
	<link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">
	<script src="/js/jquery.min.js"></script>
	<script src="/js/bootstrap.min.js"></script>
</head>
<body>
<div id="chall1-form" class="mt-5 container">
	<h1>Injection SQL #3</h1>
	<h2>Vérifiez l'existence d'un flag par id</h2>
	<div class="mt-5 justify-content-center">
	<?php if($ERROR) {
		echo "<p class='alert alert-danger'>Erreur dans la requête</p>";
	}
	if (isset($QUERY_STRING)) {
		echo "<p class='alert alert-info'>Votre dernière requête était: <code>$QUERY_STRING</code></p>";
	}
	?>
		<form method="post">
		  <div class="form-group">
			<label for="flagID">ID</label>
			<input type="number" class="form-control" id="flagID" name="flagID" placeholder="1">
		  </div>
		  <button type="submit" class="btn btn-primary">Cherchez</button>
		</form>
	</div>
</div>
<div class="mt-5 container">
	<?php
	if(isset($RESULTS) and $RESULTS) {
		print("<h2>Votre requête a retourné au moins un résultat</h2>");
	} else {
		print("<h2>Votre requête n'a retourné aucun résultat</h2>");
	}
	?>
</div>
</body>
</html>
