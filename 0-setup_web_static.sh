#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

# install Nginx if not already installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get update
    sudo apt-get -y install nginx
fi
# create necessary directories if they don't already exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo chown -R ubuntu:ubuntu /data/
#create fake html file
sudo echo "<html>
             <head>
             </head>
             <body>
                Holberton School
             </body>
           </html>" | sudo tee /data/web_static/releases/test/index.html
# create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# update Nginx config
sudo sed -i "26i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
# restart nginx
sudo service nginx restart
