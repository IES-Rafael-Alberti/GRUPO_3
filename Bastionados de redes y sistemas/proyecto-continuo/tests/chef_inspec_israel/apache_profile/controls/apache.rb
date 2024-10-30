title 'Apache Tests'


title 'Apache Server Tests'

control 'apache-01' do
  impact 1.0
  title 'Apache should be installed'
  desc 'Apache should be installed on the system'
  describe package('apache2') do
    it { should be_installed }
  end
end

control 'apache-02' do
  impact 1.0
  title 'Apache service should be running'
  desc 'The Apache service should be running'
  describe service('apache2') do
    it { should be_enabled }
    it { should be_running }
  end
end

control 'apache-03' do
  impact 1.0
  title 'Apache should be listening on port 8080'
  desc 'Apache should be listening on port 8080'
  describe port(8080) do
    it { should be_listening }
    its('processes') { should include 'apache2' }
  end
end

