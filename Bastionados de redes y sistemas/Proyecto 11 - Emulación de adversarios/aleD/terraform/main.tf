# Proyecto 11: Emulación de adversarios - Infraestructura simbólica

provider "null" {}

# Representa el firewall pfSense (instancia manual)
resource "null_resource" "pfsense" {
  provisioner "local-exec" {
    command = "echo 'pfSense configurado manualmente como firewall'"
  }
}

# Representa la máquina Ubuntu configurada con Ansible
resource "null_resource" "ubuntu" {
  provisioner "local-exec" {
    command = "echo 'Ubuntu con agente Infection Monkey y Apache instalado vía Ansible'"
  }
}

# Representa la máquina Kali usada como objetivo o atacante
resource "null_resource" "kali" {
  provisioner "local-exec" {
    command = "echo 'Kali con conexión al entorno para simular comportamiento malicioso'"
  }
}
