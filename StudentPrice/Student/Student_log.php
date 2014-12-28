<?php
	include "../Common/conn.php";

	if($_POST['phone']!='' && $_POST['passwd']!=''){
		
		$sql = 'select * from student where phone=\''.$_POST['phone'].'\' and password=\''.md5($_POST['passwd']).'\'';
		$result = mysql_query($sql);
		$row = mysql_fetch_array($result);
		if(is_array($row)){
			//echo $row['sname'];
			echo 'sucess'
			}else{
			echo 'error';
		}
	}else{
		echo 'error';
	}
?>