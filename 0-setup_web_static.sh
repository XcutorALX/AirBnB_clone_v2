#!/usr/bin/env bash
# This script sets up a web server for the deployment of web_static

test_dir="/data/web_static/releases/test/"
current_link="/data/web_static/current"
data='<html>
  <head>
  </head>
    <body>
      Holberton School
    </body>
</html>'
rules="server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;
	server_name _;

	location / {
		try_files \$uri \$uri/ =404;
		proxy_redirect off;
	}

	location /hbnb_static {
		alias /data/web_static/current;
	}
}"

if ! which nginx >/dev/null 2>&1;
then
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi

mkdir -p /data
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared
mkdir -p '/data/web_static/releases/test'
echo "$data" > '/data/web_static/releases/test/index.html'

if [ -L "$current_link" ]; 
then
    rm "$current_link"
fi

ln -sf "$test_dir" "$current_link"
chown -R ubuntu:ubuntu "/data/"
echo -e "$rules" > /etc/nginx/sites-available/default
service nginx restart
