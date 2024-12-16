### Manual de bastionado para proteger el kernel en Ubuntu Server

Este manual se centra exclusivamente en la protección del kernel en Ubuntu Server mediante la implementación de medidas de seguridad que mitiguen la explotación de procesos y refuercen la configuración del sistema.

---

#### **Requisitos previos**
- **Sistema operativo:** Ubuntu Server instalado en una máquina virtual.
- **Acceso administrativo:** Usuario con privilegios de superusuario (`root`) o permisos mediante `sudo`.
- **Conexión a internet:** Para instalar herramientas y dependencias.

---

### **1. Endurecimiento del kernel**

El kernel de Linux puede ser configurado para evitar accesos innecesarios y limitar la superficie de ataque.

1. **Configurar el acceso al archivo `/proc/kallsyms`**  
   Evita que usuarios no autorizados accedan a información sobre los símbolos del kernel:  
   ```bash
   sudo chmod 400 /proc/kallsyms
   ```

2. **Restringir el acceso al subsistema PERF**  
   Limita el uso de `perf` (herramienta de monitoreo de rendimiento del kernel) solo al usuario root:  
   ```bash
   sudo sysctl -w kernel.perf_event_paranoid=3
   ```

3. **Eliminar el acceso a `ptrace`**  
   Previene que un proceso observe o interfiera en otros procesos:  
   ```bash
   sudo sysctl -w kernel.yama.ptrace_scope=3
   ```

4. **Habilitar protección para FIFOs y archivos regulares**  
   Evita que usuarios no privilegiados manipulen archivos de sistema:  
   ```bash
   sudo sysctl -w fs.protected_regular=1
   sudo sysctl -w fs.protected_fifos=1
   ```

5. **Persistir las configuraciones de `sysctl`**  
   Añade las configuraciones anteriores al archivo `/etc/sysctl.conf` para que sean permanentes:  
   ```bash
   echo "kernel.perf_event_paranoid=3" | sudo tee -a /etc/sysctl.conf
   echo "kernel.yama.ptrace_scope=3" | sudo tee -a /etc/sysctl.conf
   echo "fs.protected_regular=1" | sudo tee -a /etc/sysctl.conf
   echo "fs.protected_fifos=1" | sudo tee -a /etc/sysctl.conf
   sudo sysctl -p
   ```

---

### **2. Eliminación de servicios innecesarios**

Los servicios que no son esenciales deben ser deshabilitados para minimizar el riesgo de ataques.

1. **Lista de servicios activos**  
   Verifica los servicios en ejecución:  
   ```bash
   sudo systemctl list-units --type=service --state=running
   ```

2. **Deshabilitar servicios innecesarios**  
   Por ejemplo, si no se utiliza `cups` (servicio de impresión):  
   ```bash
   sudo systemctl stop cups
   sudo systemctl disable cups
   ```

3. **Eliminar paquetes no requeridos**  
   Usa `autoremove` para eliminar paquetes instalados como dependencias que ya no son necesarios:  
   ```bash
   sudo apt-get autoremove
   sudo apt-get autoclean
   ```

---

### **3. Control de permisos y usuarios**

1. **Verificar permisos de usuarios y grupos**  
   Revisa las cuentas en el archivo `/etc/passwd` para identificar usuarios innecesarios:  
   ```bash
   awk -F: '($7 !~ /(\/nologin|\/false)$/) {print $1}' /etc/passwd
   ```

   Cambia el shell de usuarios innecesarios:  
   ```bash
   sudo usermod -s /usr/sbin/nologin <usuario>
   ```

2. **Deshabilitar cuentas innecesarias**  
   Por ejemplo:  
   ```bash
   sudo passwd -l <usuario>
   ```

---

### **4. Hardening de procesos**

1. **Namespaces**  
   Utiliza `unshare` para aislar procesos en sus propios espacios de sistema. Por ejemplo, para un espacio de red aislado:  
   ```bash
   sudo unshare --net /bin/bash
   ```

2. **AppArmor**  
   Habilita y configura AppArmor para restringir el comportamiento de aplicaciones:  
   ```bash
   sudo apt install apparmor apparmor-utils
   sudo aa-status
   ```

   Para restringir un servicio como NGINX:  
   ```bash
   sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx
   ```

---

### **5. Actualización del sistema**

Mantén el kernel y los paquetes actualizados para aplicar los últimos parches de seguridad:  
```bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
```

---

### **6. Validación de la seguridad**

1. **Herramientas de auditoría**  
   Utiliza `Lynis` para identificar vulnerabilidades y obtener recomendaciones:  
   ```bash
   sudo apt install lynis
   sudo lynis audit system
   ```

2. **Verificación de configuraciones del kernel**  
   Comprueba que las configuraciones de `sysctl` estén aplicadas:  
   ```bash
   sudo sysctl -a | grep -E 'perf_event_paranoid|ptrace_scope|protected'
   ```

---


    
