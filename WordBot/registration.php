#!/usr/bin/env php-cgi
<?php
$_SESSION['loggedIN'] = false;
if(isset($_POST['register'])){
    //collect form data
    $name = $_POST['username'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    //check name is set
    if($name ==''){
        $error[] = 'Username is required';
    }
    //check for a valid email address
    if(!filter_var($email, FILTER_VALIDATE_EMAIL)){
        $error[] = 'Please enter a valid email address';
    }
    $form_data = array(
       'name'  => $name,
       'email'  => $email,
       'password' => $password
    );
    //if no errors carry on
    
    if(!isset($error)){
        $file_open = fopen("all_users.csv", "a");
        fputcsv($file_open, $form_data);
        $_SESSION['loggedIN'] = true;
        header("Location: ./mainpage.shtml");
        exit();
    } else{
        echo '<p class="error">Something went wrong!</p>';
        header("Location: ./index.shtml");
        exit();
    }
}
?>