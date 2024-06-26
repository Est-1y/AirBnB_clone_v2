#!/usr/bin/env bash
# setting up web servers for web static

# Nginx installation
sudo apt-get update
sudo apt-get -y install nginx

# folders
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# HTML file formation
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html

# link formation
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# ownership allocation
sudo chown -R ubuntu:ubuntu /data/

# update
sudo sed -i 's|^.*server_name.*$|&\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n|' /etc/nginx/sites-available/default


sudo service nginx restart

exit 0
