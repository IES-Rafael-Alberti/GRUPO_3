provider "virtualbox" {
  # Solo si estás usando VBox con algún plugin
}

resource "null_resource" "ubuntu_server" {
  provisioner "local-exec" {
    command = "echo 'Aquí iría el comando para lanzar la VM o integrarte con Vagrant/VirtualBox'"
  }
}