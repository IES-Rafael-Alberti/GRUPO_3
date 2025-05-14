control 'apache' do
  title 'Verificar Apache'
  desc 'Comprobar que Apache está instalado y corriendo'

  describe package('apache2') do
    it { should be_installed }
  end

  describe service('apache2') do
    it { should be_running }
    it { should be_enabled }
  end
end

control 'tools' do
  title 'Verificar herramientas básicas'
  desc 'Comprobar que curl y net-tools están instalados'

  describe package('curl') do
    it { should be_installed }
  end

  describe package('net-tools') do
    it { should be_installed }
  end
end