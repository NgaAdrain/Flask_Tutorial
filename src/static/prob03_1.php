<?php
	include("./prob03_dbsetting.php");
	/*
	//�� �ڵ� �����۵� ����!
	${"body"}.contextmenu( function() {
	return false;
	});
	${"body"}.onselectstart( function() {
	return false;
	});
	${"body"}.ondragstart( function() {
	return false;
	});
	*/
	$ProbNum = $_POST['ProbNum'];
	$ProbText = $_POST['ProbText'];
	$ProbSel1 = $_POST['ProbSel1'];
	$ProbSel2 = $_POST['ProbSel2'];
	$ProbSel3 = $_POST['ProbSel3'];
	$ProbSel4 = $_POST['ProbSel4'];
	$ProbSel5 = $_POST['ProbSel5'];
	$ProbAns = $_POST['ProbAns'];
	$ProbSimp = $_POST['ProbSimp'];
	//form���� ���� �Է¹��� �� Ȯ���۾�
	echo "ProbNum = $ProbNum, ProbText = $ProbText, ProbSel1 = $ProbSel1,";
	echo "ProbSel2 = $ProbSel2,ProbSel3 = $ProbSel3, ProbSel4 = $ProbSel4,";
	echo "ProbSel5 = $ProbSel5,ProbAns = $ProbAns, ProbSimp = $ProbSimp";
	//������ �ߺ��� �����ϱ����� ������ �����ϸ� ����//
	$query = 
		"DELETE FROM ".TABLE_NAME." WHERE EXISTS(SELECT * FROM ".TABLE_NAME." WHERE ProbNum = $ProbNum);";
	if (mysqli_query($conn,$query)){//1. ���� �Ǽ��߾���(query�� �����ϰ� sql�� �־���(������ �Ǽ�))
		echo "Table ".TABLE_NAME." deleted successfully";
	}
	else{
		echo "Table ".TABLE_NAME." not inserted";
	}
	//�����ͻ���//
	$query ="INSERT INTO ".TABLE_NAME." (ProbNum ,ProbText ,ProbSel1 ,ProbSel2 ,ProbSel3 ,ProbSel4 ,ProbSel5 ,ProbAns ,ProbSimp) 
			VALUES ($ProbNum,'$ProbText','$ProbSel1','$ProbSel2','$ProbSel3','$ProbSel4','$ProbSel5',$ProbAns,'$ProbSimp');
		";
	if (mysqli_query($conn,$query)){//2. ������ ������ ���ÿ� �õ���
		echo "Table ".TABLE_NAME." inserted successfully";
	}
	else{
		echo "Table ".TABLE_NAME." not inserted";
	}
		
?>
