#Change the OS configuration to login with holberton
exec { 'change hard':
    command  =>  'sed -i "s/nofile 5/nofile 65535/" /etc/security/limits.conf',
    provider => 'shell',
}
exec { 'change soft':
    command  =>  'sed -i "s/nofile 4/nofile 1024/" /etc/security/limits.conf',
    provider => 'shell',
}
