<?php
	include "../Common/conn.php";
	//Student_Register
	
	$s_phone=$_POST['s_phone'];
	$s_pwd=$_POST['s_pwd'];
	$s_name=$_POST['s_name'];
	$s_school=$_POST['s_school'];
	$s_grade=$_POST['s_grade'];
	
	//$regtime=date("Y-m-d H:i:s");
	
	$sql = 'insert into student (phone,password,sname,school,grade,regtime) values ('.$s_phone.','.md5($s_pwd).','.$s_name.','.$s_school.','.$s_grade.','now()')';
	
	$result = mysql_query($sql);
	if ($result){
		echo 'sucess';
	}else{
		echo 'error';
	}
?>