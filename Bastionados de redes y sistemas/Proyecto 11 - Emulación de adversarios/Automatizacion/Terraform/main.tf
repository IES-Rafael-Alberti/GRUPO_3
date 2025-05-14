provider "virtualbox" {

}

resource "virtualbox_vm" "proyecto11_vm" {
  name   = "proyecto11"
  image  = var.vm_iso_path
  cpus   = 2
  memory = 2048

  network_adapter {
    type           = "bridged"
    host_interface = var.host_interface  # Ej: "enp3s0" o "eth0"
  }

  ssh_username = var.ssh_user
  ssh_password = var.ssh_password

  # Si usas disco base en lugar de ISO:
  # disk_path = var.disk_path
}
Vo
