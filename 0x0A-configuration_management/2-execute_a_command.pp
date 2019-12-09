# Kills a process
exec { 'pkill':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'pkill -f ./killmenow',
}
