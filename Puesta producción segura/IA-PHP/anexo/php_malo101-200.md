# 100 Ejemplos Diversos de Código PHP Malicioso

### Ejemplo 1 - SQL Injection

```php
<?php
// Código vulnerable #1
$query = "SELECT * FROM users WHERE id = $_GET['id']";
?>
```

**Vulnerabilidad:** SQL Injection  
**Descripción:** Este código permite una explotación típica del tipo sql injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 2 - XSS

```php
<?php
// Código vulnerable #2
echo "<div>" . $_GET['msg'] . "</div>";
?>
```

**Vulnerabilidad:** XSS  
**Descripción:** Este código permite una explotación típica del tipo xss por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 3 - LFI

```php
<?php
// Código vulnerable #3
include($_GET['page']);
?>
```

**Vulnerabilidad:** LFI  
**Descripción:** Este código permite una explotación típica del tipo lfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 4 - RFI

```php
<?php
// Código vulnerable #4
include('http://' . $_GET['host'] . '/malware.php');
?>
```

**Vulnerabilidad:** RFI  
**Descripción:** Este código permite una explotación típica del tipo rfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 5 - RCE

```php
<?php
// Código vulnerable #5
system($_GET['cmd']);
?>
```

**Vulnerabilidad:** RCE  
**Descripción:** Este código permite una explotación típica del tipo rce por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 6 - Command Injection

```php
<?php
// Código vulnerable #6
exec("ls " . $_GET['dir']);
?>
```

**Vulnerabilidad:** Command Injection  
**Descripción:** Este código permite una explotación típica del tipo command injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 7 - File Upload

```php
<?php
// Código vulnerable #7
move_uploaded_file($_FILES['file']['tmp_name'], '/uploads/' . $_FILES['file']['name']);
?>
```

**Vulnerabilidad:** File Upload  
**Descripción:** Este código permite una explotación típica del tipo file upload por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 8 - Insecure Deserialization

```php
<?php
// Código vulnerable #8
$data = unserialize($_GET['data']);
?>
```

**Vulnerabilidad:** Insecure Deserialization  
**Descripción:** Este código permite una explotación típica del tipo insecure deserialization por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 9 - CSRF

```php
<?php
// Código vulnerable #9
// Sin verificación CSRF
if ($_POST['change']) { cambiar_email(); }
?>
```

**Vulnerabilidad:** CSRF  
**Descripción:** Este código permite una explotación típica del tipo csrf por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 10 - Insecure Session

```php
<?php
// Código vulnerable #10
session_id($_GET['sid']); session_start();
?>
```

**Vulnerabilidad:** Insecure Session  
**Descripción:** Este código permite una explotación típica del tipo insecure session por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 11 - SQL Injection

```php
<?php
// Código vulnerable #11
$query = "SELECT * FROM users WHERE id = $_GET['id']";
?>
```

**Vulnerabilidad:** SQL Injection  
**Descripción:** Este código permite una explotación típica del tipo sql injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 12 - XSS

```php
<?php
// Código vulnerable #12
echo "<div>" . $_GET['msg'] . "</div>";
?>
```

**Vulnerabilidad:** XSS  
**Descripción:** Este código permite una explotación típica del tipo xss por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 13 - LFI

```php
<?php
// Código vulnerable #13
include($_GET['page']);
?>
```

**Vulnerabilidad:** LFI  
**Descripción:** Este código permite una explotación típica del tipo lfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 14 - RFI

```php
<?php
// Código vulnerable #14
include('http://' . $_GET['host'] . '/malware.php');
?>
```

**Vulnerabilidad:** RFI  
**Descripción:** Este código permite una explotación típica del tipo rfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 15 - RCE

```php
<?php
// Código vulnerable #15
system($_GET['cmd']);
?>
```

**Vulnerabilidad:** RCE  
**Descripción:** Este código permite una explotación típica del tipo rce por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 16 - Command Injection

```php
<?php
// Código vulnerable #16
exec("ls " . $_GET['dir']);
?>
```

**Vulnerabilidad:** Command Injection  
**Descripción:** Este código permite una explotación típica del tipo command injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 17 - File Upload

```php
<?php
// Código vulnerable #17
move_uploaded_file($_FILES['file']['tmp_name'], '/uploads/' . $_FILES['file']['name']);
?>
```

**Vulnerabilidad:** File Upload  
**Descripción:** Este código permite una explotación típica del tipo file upload por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 18 - Insecure Deserialization

```php
<?php
// Código vulnerable #18
$data = unserialize($_GET['data']);
?>
```

**Vulnerabilidad:** Insecure Deserialization  
**Descripción:** Este código permite una explotación típica del tipo insecure deserialization por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 19 - CSRF

```php
<?php
// Código vulnerable #19
// Sin verificación CSRF
if ($_POST['change']) { cambiar_email(); }
?>
```

**Vulnerabilidad:** CSRF  
**Descripción:** Este código permite una explotación típica del tipo csrf por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 20 - Insecure Session

```php
<?php
// Código vulnerable #20
session_id($_GET['sid']); session_start();
?>
```

**Vulnerabilidad:** Insecure Session  
**Descripción:** Este código permite una explotación típica del tipo insecure session por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 21 - SQL Injection

```php
<?php
// Código vulnerable #21
$query = "SELECT * FROM users WHERE id = $_GET['id']";
?>
```

**Vulnerabilidad:** SQL Injection  
**Descripción:** Este código permite una explotación típica del tipo sql injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 22 - XSS

```php
<?php
// Código vulnerable #22
echo "<div>" . $_GET['msg'] . "</div>";
?>
```

**Vulnerabilidad:** XSS  
**Descripción:** Este código permite una explotación típica del tipo xss por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 23 - LFI

```php
<?php
// Código vulnerable #23
include($_GET['page']);
?>
```

**Vulnerabilidad:** LFI  
**Descripción:** Este código permite una explotación típica del tipo lfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 24 - RFI

```php
<?php
// Código vulnerable #24
include('http://' . $_GET['host'] . '/malware.php');
?>
```

**Vulnerabilidad:** RFI  
**Descripción:** Este código permite una explotación típica del tipo rfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 25 - RCE

```php
<?php
// Código vulnerable #25
system($_GET['cmd']);
?>
```

**Vulnerabilidad:** RCE  
**Descripción:** Este código permite una explotación típica del tipo rce por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 26 - Command Injection

```php
<?php
// Código vulnerable #26
exec("ls " . $_GET['dir']);
?>
```

**Vulnerabilidad:** Command Injection  
**Descripción:** Este código permite una explotación típica del tipo command injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 27 - File Upload

```php
<?php
// Código vulnerable #27
move_uploaded_file($_FILES['file']['tmp_name'], '/uploads/' . $_FILES['file']['name']);
?>
```

**Vulnerabilidad:** File Upload  
**Descripción:** Este código permite una explotación típica del tipo file upload por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 28 - Insecure Deserialization

```php
<?php
// Código vulnerable #28
$data = unserialize($_GET['data']);
?>
```

**Vulnerabilidad:** Insecure Deserialization  
**Descripción:** Este código permite una explotación típica del tipo insecure deserialization por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 29 - CSRF

```php
<?php
// Código vulnerable #29
// Sin verificación CSRF
if ($_POST['change']) { cambiar_email(); }
?>
```

**Vulnerabilidad:** CSRF  
**Descripción:** Este código permite una explotación típica del tipo csrf por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 30 - Insecure Session

```php
<?php
// Código vulnerable #30
session_id($_GET['sid']); session_start();
?>
```

**Vulnerabilidad:** Insecure Session  
**Descripción:** Este código permite una explotación típica del tipo insecure session por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 31 - SQL Injection

```php
<?php
// Código vulnerable #31
$query = "SELECT * FROM users WHERE id = $_GET['id']";
?>
```

**Vulnerabilidad:** SQL Injection  
**Descripción:** Este código permite una explotación típica del tipo sql injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 32 - XSS

```php
<?php
// Código vulnerable #32
echo "<div>" . $_GET['msg'] . "</div>";
?>
```

**Vulnerabilidad:** XSS  
**Descripción:** Este código permite una explotación típica del tipo xss por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 33 - LFI

```php
<?php
// Código vulnerable #33
include($_GET['page']);
?>
```

**Vulnerabilidad:** LFI  
**Descripción:** Este código permite una explotación típica del tipo lfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 34 - RFI

```php
<?php
// Código vulnerable #34
include('http://' . $_GET['host'] . '/malware.php');
?>
```

**Vulnerabilidad:** RFI  
**Descripción:** Este código permite una explotación típica del tipo rfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 35 - RCE

```php
<?php
// Código vulnerable #35
system($_GET['cmd']);
?>
```

**Vulnerabilidad:** RCE  
**Descripción:** Este código permite una explotación típica del tipo rce por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 36 - Command Injection

```php
<?php
// Código vulnerable #36
exec("ls " . $_GET['dir']);
?>
```

**Vulnerabilidad:** Command Injection  
**Descripción:** Este código permite una explotación típica del tipo command injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 37 - File Upload

```php
<?php
// Código vulnerable #37
move_uploaded_file($_FILES['file']['tmp_name'], '/uploads/' . $_FILES['file']['name']);
?>
```

**Vulnerabilidad:** File Upload  
**Descripción:** Este código permite una explotación típica del tipo file upload por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 38 - Insecure Deserialization

```php
<?php
// Código vulnerable #38
$data = unserialize($_GET['data']);
?>
```

**Vulnerabilidad:** Insecure Deserialization  
**Descripción:** Este código permite una explotación típica del tipo insecure deserialization por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 39 - CSRF

```php
<?php
// Código vulnerable #39
// Sin verificación CSRF
if ($_POST['change']) { cambiar_email(); }
?>
```

**Vulnerabilidad:** CSRF  
**Descripción:** Este código permite una explotación típica del tipo csrf por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 40 - Insecure Session

```php
<?php
// Código vulnerable #40
session_id($_GET['sid']); session_start();
?>
```

**Vulnerabilidad:** Insecure Session  
**Descripción:** Este código permite una explotación típica del tipo insecure session por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 41 - SQL Injection

```php
<?php
// Código vulnerable #41
$query = "SELECT * FROM users WHERE id = $_GET['id']";
?>
```

**Vulnerabilidad:** SQL Injection  
**Descripción:** Este código permite una explotación típica del tipo sql injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 42 - XSS

```php
<?php
// Código vulnerable #42
echo "<div>" . $_GET['msg'] . "</div>";
?>
```

**Vulnerabilidad:** XSS  
**Descripción:** Este código permite una explotación típica del tipo xss por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 43 - LFI

```php
<?php
// Código vulnerable #43
include($_GET['page']);
?>
```

**Vulnerabilidad:** LFI  
**Descripción:** Este código permite una explotación típica del tipo lfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 44 - RFI

```php
<?php
// Código vulnerable #44
include('http://' . $_GET['host'] . '/malware.php');
?>
```

**Vulnerabilidad:** RFI  
**Descripción:** Este código permite una explotación típica del tipo rfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 45 - RCE

```php
<?php
// Código vulnerable #45
system($_GET['cmd']);
?>
```

**Vulnerabilidad:** RCE  
**Descripción:** Este código permite una explotación típica del tipo rce por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 46 - Command Injection

```php
<?php
// Código vulnerable #46
exec("ls " . $_GET['dir']);
?>
```

**Vulnerabilidad:** Command Injection  
**Descripción:** Este código permite una explotación típica del tipo command injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 47 - File Upload

```php
<?php
// Código vulnerable #47
move_uploaded_file($_FILES['file']['tmp_name'], '/uploads/' . $_FILES['file']['name']);
?>
```

**Vulnerabilidad:** File Upload  
**Descripción:** Este código permite una explotación típica del tipo file upload por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 48 - Insecure Deserialization

```php
<?php
// Código vulnerable #48
$data = unserialize($_GET['data']);
?>
```

**Vulnerabilidad:** Insecure Deserialization  
**Descripción:** Este código permite una explotación típica del tipo insecure deserialization por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 49 - CSRF

```php
<?php
// Código vulnerable #49
// Sin verificación CSRF
if ($_POST['change']) { cambiar_email(); }
?>
```

**Vulnerabilidad:** CSRF  
**Descripción:** Este código permite una explotación típica del tipo csrf por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 50 - Insecure Session

```php
<?php
// Código vulnerable #50
session_id($_GET['sid']); session_start();
?>
```

**Vulnerabilidad:** Insecure Session  
**Descripción:** Este código permite una explotación típica del tipo insecure session por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 51 - SQL Injection

```php
<?php
// Código vulnerable #51
$query = "SELECT * FROM users WHERE id = $_GET['id']";
?>
```

**Vulnerabilidad:** SQL Injection  
**Descripción:** Este código permite una explotación típica del tipo sql injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 52 - XSS

```php
<?php
// Código vulnerable #52
echo "<div>" . $_GET['msg'] . "</div>";
?>
```

**Vulnerabilidad:** XSS  
**Descripción:** Este código permite una explotación típica del tipo xss por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 53 - LFI

```php
<?php
// Código vulnerable #53
include($_GET['page']);
?>
```

**Vulnerabilidad:** LFI  
**Descripción:** Este código permite una explotación típica del tipo lfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 54 - RFI

```php
<?php
// Código vulnerable #54
include('http://' . $_GET['host'] . '/malware.php');
?>
```

**Vulnerabilidad:** RFI  
**Descripción:** Este código permite una explotación típica del tipo rfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 55 - RCE

```php
<?php
// Código vulnerable #55
system($_GET['cmd']);
?>
```

**Vulnerabilidad:** RCE  
**Descripción:** Este código permite una explotación típica del tipo rce por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 56 - Command Injection

```php
<?php
// Código vulnerable #56
exec("ls " . $_GET['dir']);
?>
```

**Vulnerabilidad:** Command Injection  
**Descripción:** Este código permite una explotación típica del tipo command injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 57 - File Upload

```php
<?php
// Código vulnerable #57
move_uploaded_file($_FILES['file']['tmp_name'], '/uploads/' . $_FILES['file']['name']);
?>
```

**Vulnerabilidad:** File Upload  
**Descripción:** Este código permite una explotación típica del tipo file upload por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 58 - Insecure Deserialization

```php
<?php
// Código vulnerable #58
$data = unserialize($_GET['data']);
?>
```

**Vulnerabilidad:** Insecure Deserialization  
**Descripción:** Este código permite una explotación típica del tipo insecure deserialization por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 59 - CSRF

```php
<?php
// Código vulnerable #59
// Sin verificación CSRF
if ($_POST['change']) { cambiar_email(); }
?>
```

**Vulnerabilidad:** CSRF  
**Descripción:** Este código permite una explotación típica del tipo csrf por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 60 - Insecure Session

```php
<?php
// Código vulnerable #60
session_id($_GET['sid']); session_start();
?>
```

**Vulnerabilidad:** Insecure Session  
**Descripción:** Este código permite una explotación típica del tipo insecure session por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 61 - SQL Injection

```php
<?php
// Código vulnerable #61
$query = "SELECT * FROM users WHERE id = $_GET['id']";
?>
```

**Vulnerabilidad:** SQL Injection  
**Descripción:** Este código permite una explotación típica del tipo sql injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 62 - XSS

```php
<?php
// Código vulnerable #62
echo "<div>" . $_GET['msg'] . "</div>";
?>
```

**Vulnerabilidad:** XSS  
**Descripción:** Este código permite una explotación típica del tipo xss por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 63 - LFI

```php
<?php
// Código vulnerable #63
include($_GET['page']);
?>
```

**Vulnerabilidad:** LFI  
**Descripción:** Este código permite una explotación típica del tipo lfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 64 - RFI

```php
<?php
// Código vulnerable #64
include('http://' . $_GET['host'] . '/malware.php');
?>
```

**Vulnerabilidad:** RFI  
**Descripción:** Este código permite una explotación típica del tipo rfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 65 - RCE

```php
<?php
// Código vulnerable #65
system($_GET['cmd']);
?>
```

**Vulnerabilidad:** RCE  
**Descripción:** Este código permite una explotación típica del tipo rce por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 66 - Command Injection

```php
<?php
// Código vulnerable #66
exec("ls " . $_GET['dir']);
?>
```

**Vulnerabilidad:** Command Injection  
**Descripción:** Este código permite una explotación típica del tipo command injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 67 - File Upload

```php
<?php
// Código vulnerable #67
move_uploaded_file($_FILES['file']['tmp_name'], '/uploads/' . $_FILES['file']['name']);
?>
```

**Vulnerabilidad:** File Upload  
**Descripción:** Este código permite una explotación típica del tipo file upload por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 68 - Insecure Deserialization

```php
<?php
// Código vulnerable #68
$data = unserialize($_GET['data']);
?>
```

**Vulnerabilidad:** Insecure Deserialization  
**Descripción:** Este código permite una explotación típica del tipo insecure deserialization por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 69 - CSRF

```php
<?php
// Código vulnerable #69
// Sin verificación CSRF
if ($_POST['change']) { cambiar_email(); }
?>
```

**Vulnerabilidad:** CSRF  
**Descripción:** Este código permite una explotación típica del tipo csrf por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 70 - Insecure Session

```php
<?php
// Código vulnerable #70
session_id($_GET['sid']); session_start();
?>
```

**Vulnerabilidad:** Insecure Session  
**Descripción:** Este código permite una explotación típica del tipo insecure session por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 71 - SQL Injection

```php
<?php
// Código vulnerable #71
$query = "SELECT * FROM users WHERE id = $_GET['id']";
?>
```

**Vulnerabilidad:** SQL Injection  
**Descripción:** Este código permite una explotación típica del tipo sql injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 72 - XSS

```php
<?php
// Código vulnerable #72
echo "<div>" . $_GET['msg'] . "</div>";
?>
```

**Vulnerabilidad:** XSS  
**Descripción:** Este código permite una explotación típica del tipo xss por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 73 - LFI

```php
<?php
// Código vulnerable #73
include($_GET['page']);
?>
```

**Vulnerabilidad:** LFI  
**Descripción:** Este código permite una explotación típica del tipo lfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 74 - RFI

```php
<?php
// Código vulnerable #74
include('http://' . $_GET['host'] . '/malware.php');
?>
```

**Vulnerabilidad:** RFI  
**Descripción:** Este código permite una explotación típica del tipo rfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 75 - RCE

```php
<?php
// Código vulnerable #75
system($_GET['cmd']);
?>
```

**Vulnerabilidad:** RCE  
**Descripción:** Este código permite una explotación típica del tipo rce por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 76 - Command Injection

```php
<?php
// Código vulnerable #76
exec("ls " . $_GET['dir']);
?>
```

**Vulnerabilidad:** Command Injection  
**Descripción:** Este código permite una explotación típica del tipo command injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 77 - File Upload

```php
<?php
// Código vulnerable #77
move_uploaded_file($_FILES['file']['tmp_name'], '/uploads/' . $_FILES['file']['name']);
?>
```

**Vulnerabilidad:** File Upload  
**Descripción:** Este código permite una explotación típica del tipo file upload por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 78 - Insecure Deserialization

```php
<?php
// Código vulnerable #78
$data = unserialize($_GET['data']);
?>
```

**Vulnerabilidad:** Insecure Deserialization  
**Descripción:** Este código permite una explotación típica del tipo insecure deserialization por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 79 - CSRF

```php
<?php
// Código vulnerable #79
// Sin verificación CSRF
if ($_POST['change']) { cambiar_email(); }
?>
```

**Vulnerabilidad:** CSRF  
**Descripción:** Este código permite una explotación típica del tipo csrf por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 80 - Insecure Session

```php
<?php
// Código vulnerable #80
session_id($_GET['sid']); session_start();
?>
```

**Vulnerabilidad:** Insecure Session  
**Descripción:** Este código permite una explotación típica del tipo insecure session por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 81 - SQL Injection

```php
<?php
// Código vulnerable #81
$query = "SELECT * FROM users WHERE id = $_GET['id']";
?>
```

**Vulnerabilidad:** SQL Injection  
**Descripción:** Este código permite una explotación típica del tipo sql injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 82 - XSS

```php
<?php
// Código vulnerable #82
echo "<div>" . $_GET['msg'] . "</div>";
?>
```

**Vulnerabilidad:** XSS  
**Descripción:** Este código permite una explotación típica del tipo xss por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 83 - LFI

```php
<?php
// Código vulnerable #83
include($_GET['page']);
?>
```

**Vulnerabilidad:** LFI  
**Descripción:** Este código permite una explotación típica del tipo lfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 84 - RFI

```php
<?php
// Código vulnerable #84
include('http://' . $_GET['host'] . '/malware.php');
?>
```

**Vulnerabilidad:** RFI  
**Descripción:** Este código permite una explotación típica del tipo rfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 85 - RCE

```php
<?php
// Código vulnerable #85
system($_GET['cmd']);
?>
```

**Vulnerabilidad:** RCE  
**Descripción:** Este código permite una explotación típica del tipo rce por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 86 - Command Injection

```php
<?php
// Código vulnerable #86
exec("ls " . $_GET['dir']);
?>
```

**Vulnerabilidad:** Command Injection  
**Descripción:** Este código permite una explotación típica del tipo command injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 87 - File Upload

```php
<?php
// Código vulnerable #87
move_uploaded_file($_FILES['file']['tmp_name'], '/uploads/' . $_FILES['file']['name']);
?>
```

**Vulnerabilidad:** File Upload  
**Descripción:** Este código permite una explotación típica del tipo file upload por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 88 - Insecure Deserialization

```php
<?php
// Código vulnerable #88
$data = unserialize($_GET['data']);
?>
```

**Vulnerabilidad:** Insecure Deserialization  
**Descripción:** Este código permite una explotación típica del tipo insecure deserialization por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 89 - CSRF

```php
<?php
// Código vulnerable #89
// Sin verificación CSRF
if ($_POST['change']) { cambiar_email(); }
?>
```

**Vulnerabilidad:** CSRF  
**Descripción:** Este código permite una explotación típica del tipo csrf por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 90 - Insecure Session

```php
<?php
// Código vulnerable #90
session_id($_GET['sid']); session_start();
?>
```

**Vulnerabilidad:** Insecure Session  
**Descripción:** Este código permite una explotación típica del tipo insecure session por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 91 - SQL Injection

```php
<?php
// Código vulnerable #91
$query = "SELECT * FROM users WHERE id = $_GET['id']";
?>
```

**Vulnerabilidad:** SQL Injection  
**Descripción:** Este código permite una explotación típica del tipo sql injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 92 - XSS

```php
<?php
// Código vulnerable #92
echo "<div>" . $_GET['msg'] . "</div>";
?>
```

**Vulnerabilidad:** XSS  
**Descripción:** Este código permite una explotación típica del tipo xss por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 93 - LFI

```php
<?php
// Código vulnerable #93
include($_GET['page']);
?>
```

**Vulnerabilidad:** LFI  
**Descripción:** Este código permite una explotación típica del tipo lfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 94 - RFI

```php
<?php
// Código vulnerable #94
include('http://' . $_GET['host'] . '/malware.php');
?>
```

**Vulnerabilidad:** RFI  
**Descripción:** Este código permite una explotación típica del tipo rfi por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 95 - RCE

```php
<?php
// Código vulnerable #95
system($_GET['cmd']);
?>
```

**Vulnerabilidad:** RCE  
**Descripción:** Este código permite una explotación típica del tipo rce por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 96 - Command Injection

```php
<?php
// Código vulnerable #96
exec("ls " . $_GET['dir']);
?>
```

**Vulnerabilidad:** Command Injection  
**Descripción:** Este código permite una explotación típica del tipo command injection por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 97 - File Upload

```php
<?php
// Código vulnerable #97
move_uploaded_file($_FILES['file']['tmp_name'], '/uploads/' . $_FILES['file']['name']);
?>
```

**Vulnerabilidad:** File Upload  
**Descripción:** Este código permite una explotación típica del tipo file upload por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 98 - Insecure Deserialization

```php
<?php
// Código vulnerable #98
$data = unserialize($_GET['data']);
?>
```

**Vulnerabilidad:** Insecure Deserialization  
**Descripción:** Este código permite una explotación típica del tipo insecure deserialization por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 99 - CSRF

```php
<?php
// Código vulnerable #99
// Sin verificación CSRF
if ($_POST['change']) { cambiar_email(); }
?>
```

**Vulnerabilidad:** CSRF  
**Descripción:** Este código permite una explotación típica del tipo csrf por no validar ni sanitizar adecuadamente la entrada del usuario.
---

### Ejemplo 100 - Insecure Session

```php
<?php
// Código vulnerable #100
session_id($_GET['sid']); session_start();
?>
```

**Vulnerabilidad:** Insecure Session  
**Descripción:** Este código permite una explotación típica del tipo insecure session por no validar ni sanitizar adecuadamente la entrada del usuario.
---
