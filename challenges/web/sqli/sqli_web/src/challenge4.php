<?php
include("includes/chal4.php");
?>

<html>
<head>
	<link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">
	<script src="/js/jquery.min.js"></script>
	<script src="/js/bootstrap.min.js"></script>
</head>
<body>
<div id="chall1-form" class="mt-5 container">
	<h1>Injection SQL #4</h1>
	<h2><em>&#x3C;Insert pretense for challenge here&#x3Ca;</em> d'un flag par id</h2>
	<div class="mt-5 justify-content-center">
	<?php if (isset($QUERY_STRING)) {
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
</body>
</html>
