# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Please don't change it unless you know what you're doing.
VAGRANTFILE_API_VERSION = "2"

Vagrant.require_version ">= 1.8.1"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  config.vm.provider "virtualbox" do |vb|
    vb.memory = 4096
    vb.cpus = 2
  end

  config.vm.provision :shell, inline: "cat /vagrant/hosts > /etc/hosts"
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Set up machine
  config.vm.define "docker-django-jwt", primary: true do |node|
    node.vm.box = "ubuntu/trusty64"
    node.vm.hostname = "docker-django-jwt"
    node.vm.network "private_network", ip: "192.168.33.112"
  end

end
