#!/usr/bin/env bash
# Script to further set up a web server for web_static
dpkg -l nginx
if [ $? -ne 0 ]
then
    apt-get update
    apt-get install -y nginx
fi
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test/
echo "This is a test" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i 's|server_name _;|server_name _;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/hbnb_static;\n\t}\n|' /etc/nginx/sites-available/default
service nginx restart
