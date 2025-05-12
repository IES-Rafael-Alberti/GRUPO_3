### Ejemplo 1: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 2: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 3: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 4: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 5: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 6: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 7: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 8: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 9: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 10: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 11: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 12: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 13: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 14: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 15: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 16: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 17: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 18: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 19: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 20: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 21: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 22: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 23: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 24: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 25: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 26: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 27: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 28: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 29: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 30: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 31: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 32: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 33: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 34: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 35: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 36: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 37: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 38: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 39: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 40: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 41: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 42: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 43: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 44: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 45: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 46: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 47: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 48: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 49: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 50: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 51: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 52: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 53: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 54: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 55: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 56: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 57: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 58: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 59: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 60: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 61: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 62: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 63: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 64: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 65: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 66: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 67: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 68: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 69: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 70: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 71: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 72: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 73: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 74: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 75: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 76: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 77: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 78: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 79: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 80: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 81: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 82: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 83: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 84: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 85: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 86: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 87: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 88: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 89: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 90: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 91: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 92: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 93: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 94: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 95: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```

### Ejemplo 96: Escape de salida para prevenir XSS

```php
<?php
$comentario = $_GET['comentario'] ?? '';
echo htmlspecialchars($comentario, ENT_QUOTES, 'UTF-8');
?>
```

### Ejemplo 97: Subida segura de archivos

```php
<?php
$permitidos = ['image/jpeg', 'image/png'];
if (in_array($_FILES['archivo']['type'], $permitidos)) {
    $ruta = 'uploads/' . basename($_FILES['archivo']['name']);
    move_uploaded_file($_FILES['archivo']['tmp_name'], $ruta);
} else {
    echo 'Tipo de archivo no permitido';
}
?>
```

### Ejemplo 98: Autenticación con password_hash

```php
<?php
$contraseña = $_POST['password'];
$hash = password_hash($contraseña, PASSWORD_DEFAULT);
// Verificación
if (password_verify($contraseña, $hash)) {
    echo 'Contraseña válida';
} else {
    echo 'Contraseña incorrecta';
}
?>
```

### Ejemplo 99: Uso de Content Security Policy

```php
<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'");
?>
```

### Ejemplo 100: Protección contra CSRF

```php
<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        die('CSRF token inválido');
    }
}
?>
<form method="POST">
    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($_SESSION['csrf_token']); ?>">
    <input type="submit" value="Enviar">
</form>
```