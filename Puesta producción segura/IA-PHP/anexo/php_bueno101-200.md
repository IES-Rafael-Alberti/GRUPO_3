### Ejemplo 1: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 2: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 3: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 4: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 5: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 6: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 7: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 8: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 9: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 10: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 11: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 12: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 13: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 14: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 15: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 16: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 17: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 18: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 19: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 20: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 21: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 22: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 23: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 24: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 25: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 26: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 27: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 28: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 29: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 30: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 31: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 32: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 33: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 34: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 35: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 36: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 37: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 38: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 39: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 40: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 41: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 42: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 43: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 44: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 45: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 46: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 47: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 48: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 49: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 50: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 51: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 52: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 53: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 54: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 55: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 56: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 57: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 58: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 59: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 60: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 61: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 62: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 63: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 64: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 65: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 66: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 67: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 68: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 69: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 70: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 71: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 72: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 73: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 74: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 75: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 76: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 77: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 78: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 79: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 80: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 81: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 82: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 83: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 84: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 85: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 86: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 87: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 88: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 89: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 90: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 91: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 92: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 93: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 94: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 95: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 96: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 97: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 98: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 99: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```


### Ejemplo 100: Validación y escape de entrada de usuario

```php
<?php
// Conexión a base de datos usando PDO (práctica segura)
$dsn = 'mysql:host=localhost;dbname=mi_base_de_datos';
$usuario = 'usuario';
$contraseña = 'contraseña';
$opciones = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $usuario, $contraseña, $opciones);
} catch (PDOException $e) {
    die('Error de conexión: ' . $e->getMessage());
}

// Validación de entrada
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false) {
    die('ID inválido');
}

// Consulta preparada (previene inyección SQL)
$stmt = $pdo->prepare('SELECT * FROM usuarios WHERE id = :id');
$stmt->execute(['id' => $id]);
$usuario = $stmt->fetch();

if ($usuario) {
    echo htmlspecialchars($usuario['nombre']);
} else {
    echo 'Usuario no encontrado';
}
?>
```
