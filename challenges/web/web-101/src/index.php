<?php
  header("X-Secret-Flag-4: FLAG-6a11afa3a060b06ac714a2f38d6b7147");

  $data_file_path = "./013b65adf5580e21.json";
  $data = json_decode(file_get_contents($data_file_path), true);
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Awesome Blog</title>
</head>
<body>
  <!-- This is HTML comment. -->
  <!-- Sometimes is contains important information that the programmer might have left. -->
  <h1>My Awesome Blog</h1>
  <p>Hi, my name is John Doe! I love cats, programming and also flags.</p>
  <hr>
  <?php if (isset($_GET['id'])) { ?>
    <?php
      $title = "Post not found! :(";
      $content = "This is sad, maybe change the param 'id' in the URL?";
      foreach ($data['posts'] as $post) {
        if ($post['id'] === $_GET['id']) {
          $title = $post['title'];
          $content = $post['content'];
        }
      }
    ?>
  <h2><?php echo $title ?></h2>
  <p><?php echo $content ?></p>
  <?php  } else { ?>
    <h2>Posts</h2>
    <ul>
      <?php
        foreach ($data['posts'] as $post) {
          if (!$post['draft']) {
            $id = $post['id'];
            $title = $post['title'];
            echo "<li><a href='?id=$id'>$title</a></li>" . PHP_EOL;
          }
        }
      ?>
    </ul>
  <?php } ?>
  <footer>© My Awesome Blog</footer>
  <!-- Secret Flag 1: FLAG-03f06d335e77ccba975315b27a5e4493 -->
</body>
</html>
