<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Awesome Blog | Admin section</title>
</head>
<body>
  <h1>My Awesome Blog | <u>Admin section</u></h1>
  <p>This is in beta.</p>
  <p>This is to help admin debug the code source of a <i>page</i>.</p>
  <hr>
  <h4>Admin Pages:</h4>
  <ul>
    <li>
      <a href="index.php">index.php</a>
    </li>
    <li>
      <a href="test.php">test.php</a>
    </li>
    <!-- TODO: List the other pages. -->
  </ul>
  <hr>
  <code>
    <!-- To use the debug mode specify the page. -->
    <!-- Example: ?page=test.php -->
  <?php
  // I heard this could cause a security vulnerability called: Local File Inclusion (LFI).
  // Maybe I should look into it... For now only allow files in this directory.
  // Secret Flag 5: FLAG-9fd42bed331fdbc7346c1b7a02043919
  $pages = array("index.php", "test.php");
  if (isset($_GET['page']) && in_array($_GET['page'], $pages)) {
    highlight_string(file_get_contents($_GET['page']));
  }
  ?>
  </code>
  <hr>
  <footer>© My Awesome Blog</footer>
</body>
</html>
