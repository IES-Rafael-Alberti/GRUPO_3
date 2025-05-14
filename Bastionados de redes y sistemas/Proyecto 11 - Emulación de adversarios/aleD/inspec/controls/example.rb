control 'apache2' do
  impact 1.0
  title 'Verificar instalación y estado de apache2'
  desc 'Asegura que apache2 esté correctamente instalado y en ejecución'

  describe package('apache2') do
    it { should be_installed }
  end

  describe service('apache2') do
    it { should be_running }
    it { should be_enabled }
  end

  describe port(80) do
    it { should be_listening }
  end
end

control 'paquetes' do
  impact 0.7
  title 'Verificar paquetes adicionales instalados'
  desc 'Comprueba que htop, figlet y net-tools están presentes'

  %w(htop figlet net-tools).each do |pkg|
    describe package(pkg) do
      it { should be_installed }
    end
  end
end
