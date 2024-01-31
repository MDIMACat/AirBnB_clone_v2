#!/usr/bin/env bash
#Sets up your web servers for deployment

sudo apt-get update
sudo apt-get install nginx -y

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p  /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;

    error_page 404 /404.html;

    location /404.html {
        root /var/www/html/;
        internal;
    }

    location / {
        add_header X-Served-By \$hostname;
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
}
" | sudo tee /etc/nginx/sites-available/default

sudo service nginx restart
