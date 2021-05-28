# Debugging four
exec { 'ulimit':
    path     => ['/usr/bin'],
    command  =>  'sed -i "s/15/2000/" /etc/default/nginx;
                sudo service nginx restart',
    provider => 'shell',
}
