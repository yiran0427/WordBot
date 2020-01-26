#!/usr/bin/env php-cgi

<?php

$username = $_POST['username'];
$password = $_POST['password'];
$message = "Login Failed!";

if (!strlen($username) || !strlen($password)) {
    echo '<p class="error">Login Failed!</p>';
    header("Location: ./index.shtml");
    exit();
}

$success = false;

$handle = fopen("all_users.csv", "r");
while (($data = fgetcsv($handle)) !== FALSE) {
    if ($data[0] == $username && $data[2] == $password) {
        $success = true;
        break;
    }
}
fclose($handle);
$_SESSION['loggedIN'] = false;
if ($success) {
    header("Location: ./mainpage.shtml");
    $_SESSION['loggedIN'] = true;
    exit();
} else {
    echo "<script type='text/javascript'>alert('$message');</script>";
    header("Location: ./index.shtml");
    exit();
}
?>