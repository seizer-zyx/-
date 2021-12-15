<?php
highlight_file(__FILE__);
error_reporting(0);
$flag = 'flag.php';
if(isset($_GET['flag'])){
    $flag = $_GET['flag'];
}
include($flag);
?>