<?php
//admin_init contains all the db methods I use in this script
require_once('admin_init.php');

$companies = json_decode(file_get_contents('company_info_with_cvr.json'));

$results = [];
$i = 0;

foreach ($companies as $company){
	//No, I'm not showing you the inner workings of my companys database. This SQL expression
	//should get the number of cases a client has ever had.
	$sql = "SELECT COUNT(*) AS sager FROM .........".$company->cvr;
	$result = $db->queryEx($sql);

	if ($result && $result->num_rows > 0){
		while ($row = $result->fetch_object()){
			$results[$company->industrycode]['industry'] = $company->industry;
			$cases = &$results[$company->industrycode]['cases'];
			$cases += $row->sager;
			$comp = &$results[$company->industrycode]['companies'];
			$comp++;
		}
	}

}

foreach($results as &$result){
	$result['average'] = $result['cases']/$result['companies'];
}

uasort($results, function($a,$b){
	$a=$a['average'];
	$b=$b['average'];
	if ($a == $b) {
        return 0;
    }
    return ($a < $b) ? 1 : -1;
});

$out = fopen('php://output', 'w');
fputcsv($out, ['Branchekode','Gennemsnit'],';');
echo '<br>';
foreach($results as $result){
	fputcsv($out, [utf8_decode($result['industry']),number_format($result['average'],2,',','')],';');
	echo '<br>';
}
fclose($out);