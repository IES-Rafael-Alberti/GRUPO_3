control 'apache2' do
  impact 1.0
  title 'Comprobar que apache está instalado y en funcionamiento'

  describe package('apache2') do
    it { should be_installed }
  end

  describe service('apache2') do
    it { should be_enabled }
    it { should be_running }
  end

  describe port(80) do
    it { should be_listening }
  end
end
