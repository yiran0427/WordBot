#!/usr/bin/env php-cgi
<?php
if ($_SESSION['loggedIN'] == false){
	header('Location: ./index.shtml');
}
?>