<?php
// api.php
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['name'])) {
    $name = htmlspecialchars($_GET['name']);
    echo json_encode(['message' => "Hello, $name!"]);
} else {
    echo json_encode(['error' => 'Invalid request']);
}
?>
