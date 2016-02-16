<html>
<head>
<meta charset="UTF-8" />
<title>PHP and Python Test</title>
</head>

<link href="test.css" rel="stylesheet">
<?php
if (isset($_POST['CallTyler']))
{
exec("python lifesizedial.py");
}
if (isset($_POST['Input2']))
{
exec("python input2telnet.py");
}
?>
<form method="post">
<button name="CallTyler">Call Tyler</button>&nbsp;
<button name="Input2">Input Two</button><br>
<button name="Test3">Test3</button><br>

</form>
</html>
