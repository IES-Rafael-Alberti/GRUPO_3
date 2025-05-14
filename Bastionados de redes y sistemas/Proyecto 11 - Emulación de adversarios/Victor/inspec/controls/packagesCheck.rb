control 'paquetes-1.0' do
  impact 0.7
  title 'Comprobar net-tools y curl'
  desc 'Verificar si están instalados los paquetes net-tools y curl'

  describe package('net-tools') do
    it { should be_installed }
  end

  describe package('curl') do
    it { should be_installed }
  end
end