<?php
include("includes/chal1.php");
?>

<html>
<head>
	<link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">
	<script src="/js/jquery.min.js"></script>
	<script src="/js/bootstrap.min.js"></script>
</head>
<body>
<div id="chall1-form" class="mt-5 container">
	<h1>Injection SQL #1</h1>
	<h2>Cherchez un post par id</h2>
	<div class="mt-5 justify-content-center">
	<?php if(isset($ERROR)) {
		echo "<p class='alert alert-danger'>$ERROR</p>";
	}
	if (isset($QUERY_STRING)) {
		echo "<p class='alert alert-info'>Votre dernière requête était: <code>$QUERY_STRING</code></p>";
	}
	?>
		<form method="post">
		  <div class="form-group">
			<label for="msgID">ID</label>
			<input type="number" class="form-control" id="msgID" name="msgID" placeholder="1">
		  </div>
		  <button type="submit" class="btn btn-primary">Cherchez</button>
		</form>
	</div>
</div>
<div class="mt-5 container">
	<h2>Résultats de votre requête</h2>
	<table class="table table-hover">
		<thead>
			<tr>
				<th scope="col">Id</th>
				<th scope="col">Author</th>
				<th scope="col">Content</th>
				<th scope="col">Post_date</th>
			</tr>
		</thead>
		<tbody>
		<?php
			if(isset($RESULT)) {
				foreach($RESULT as $line) {
					printf($ROW_FORMAT, $line[0], $line[1], $line[2], $line[3]);
				}
			}
		?>
		</tbody>
	</table>
</div>
</body>
</html>
