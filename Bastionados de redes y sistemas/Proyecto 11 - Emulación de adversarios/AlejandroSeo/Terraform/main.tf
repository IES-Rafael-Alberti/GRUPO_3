terraform {
  required_providers {
    vagrant = {
      source  = "bmatcuk/vagrant"
      version = "~> 0.2"
    }
  }
}

provider "vagrant" {}

# FIREWALL (pfSense)
resource "vagrant_vm" "firewall" {
  name = "firewall"
  box  = "bento/pfsense"

  vagrantfile = <<EOF
Vagrant.configure("2") do |config|
  config.vm.box = "bento/pfsense"
  config.vm.hostname = "firewall"

  # Red interna 
  config.vm.network "private_network", ip: "192.168.56.1"

  # Red externa 
  config.vm.network "public_network", bridge: "wlp2s0", auto_config: true

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 512
    vb.cpus = 1
  end
end
EOF
}

# VÍCTIMA (Ubuntu)
resource "vagrant_vm" "victima" {
  name = "victima"
  box  = "ubuntu/jammy64"

  vagrantfile = <<EOF
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.hostname = "victima"
  config.vm.network "private_network", ip: "192.168.56.3"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 2048
    vb.cpus = 2
  end
end
EOF
}

# ATACANTE (Kali Linux)
resource "vagrant_vm" "atacante" {
  name = "atacante"
  box  = "kalilinux/rolling"

  vagrantfile = <<EOF
Vagrant.configure("2") do |config|
  config.vm.box = "kalilinux/rolling"
  config.vm.hostname = "atacante"
  config.vm.network "private_network", ip: "192.168.56.4"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 2048
    vb.cpus = 2
  end
end
EOF
}
