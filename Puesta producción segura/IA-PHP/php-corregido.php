<?php
// Protección contra CSRF: Usa tokens de autenticación temporal o comparación de headers.
if ($_SERVER['HTTP_REFERER'] != 'https://tuapp.php') {
    // Redirigir o mostrar error si no viene del mismo origen
}

// Validar entrada de usuario
function validarUsuario($nombre, $clave) {
    // Escaping de HTML y caracteres especiales
    $nombreSanitizado = htmlspecialchars(strip_tags($nombre));
    $claveSanitizada = htmlspecialchars(strip_tags($clave));

    // Implementación de validación de SQL
    try {
        $conexion = new PDO('mysql:host=localhost;dbname=database', 'user', 'pass');
        $stmt = $conexion->prepare("INSERT INTO usuarios (nombre, clave) VALUES (?, ?)");
        $stmt->bind_param('s', $nombreSanitizado);
        $stmt->bind_param('s', sha1($claveSanitizada)); // Usa SHA-1 o algoritmo seguro
        $stmt->execute();
        $conexion->close();
    } catch (Exception $e) {
        echo "Error de conexión: " . $e->getMessage();
    }
}

// Protección contra XSS en la salida
function muestraResultado($busqueda) {
    $busquedaSanitizada = htmlspecialchars($busqueda);
    echo "<h1>Resultados para: $busquedaSanitizada</h1>";
}