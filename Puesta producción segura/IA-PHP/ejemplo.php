<?php
session_start();

$conn = new mysqli("localhost", "root", "", "tienda");

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $usuario = $_POST['usuario'];
    $clave = $_POST['clave'];

    $sql = "SELECT * FROM usuarios WHERE nombre = '$usuario' AND clave = '$clave'";
    $resultado = $conn->query($sql);

    if ($resultado->num_rows > 0) {
        $_SESSION['usuario'] = $usuario;
        header("Location: dashboard.php");
        exit;
    } else {
        echo "Credenciales inválidas";
    }
}

if (isset($_GET['busqueda'])) {
    $busqueda = $_GET['busqueda'];
    echo "<h1>Resultados para: $busqueda</h1>";
}

function registrarUsuario($nombre, $clave) {
    global $conn;
    $stmt = $conn->prepare("INSERT INTO usuarios (nombre, clave) VALUES (?, ?)");
    $clave_hash = password_hash($clave, PASSWORD_BCRYPT);
    $stmt->bind_param("ss", $nombre, $clave_hash);
    $stmt->execute();
    $stmt->close();
}

function cerrarSesion() {
    session_unset();
    session_destroy();
    header("Location: index.php");
}
?>