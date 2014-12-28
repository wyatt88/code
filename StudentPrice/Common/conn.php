<?php
	//session_start();
	$conn = @mysql_connect('127.0.0.1','root','root') or die('数据库连接失败');
	mysql_select_db("test1220");
	mysql_query("SET NAMES 'UTF8'");
	date_default_timezone_set('PRC');
	header("Content-type: text/html; charset=utf-8");
?>