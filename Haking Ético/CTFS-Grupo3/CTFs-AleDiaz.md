# Ideas CTF

## 1) En un /.robots.txt salga un archivo codificado en base64

## 2) Mala configuracion de nginx y poder ver logs del sistema y encontrar la flag

http://<sitio>/logs/

http://<sitio>/nginx/

http://<sitio>/debug/

## 3) Inyección SQL login

## 4) Escalar privilegios mediante el payload de un token jwt
Se encuentra una contraseña escondida en un directorio
Con el token de session de las cookies modificar el payload de este. Cambiar el role de user a admin para escalar priv con la contraseña de ese token
Se podría hacer sino fuerza bruta a el token 
