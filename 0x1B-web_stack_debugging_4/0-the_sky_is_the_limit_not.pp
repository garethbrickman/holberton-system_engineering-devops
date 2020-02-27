# Fixes file extension typo in WordPress settings config
exec { 'fix-ulimit':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "sed -i 's/15/4096/g' /etc/default/nginx",
}
# Restarts nginx
exec { 'nginx-restart':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'sudo service nginx restart',
}
