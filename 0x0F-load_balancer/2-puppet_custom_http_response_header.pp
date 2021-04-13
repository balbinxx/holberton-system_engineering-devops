# Create a custom HTTP header response
exec {'Http_header':
    command  => 'sudo apt-get update -y; 
    sudo apt-get -y install nginx; 
    sed -i "20 i add_header X-Served-By \"\$HOSTNAME\";" /etc/nginx/sites-available/default; 
    sudo service nginx restart',
    provider => 'shell',
}
