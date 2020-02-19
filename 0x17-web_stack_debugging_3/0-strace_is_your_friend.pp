# Fixes file extension typo in WordPress settings config
exec { 'fix-typo':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
# Restarts Apache2
exec { 'apache-restart':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'sudo service apache2 restart',
}
