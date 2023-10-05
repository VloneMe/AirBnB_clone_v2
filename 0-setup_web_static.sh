#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

# 1. Install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# 2. Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# 3. Create a fake HTML file for testing
echo "<html>
<head></head>
<body>Test Page</body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null 2>&1

# 4. Create a symbolic link to /data/web_static/releases/test/
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

# 5. Give ownership of /data/ to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data

# 6. Update Nginx configuration to serve content from /data/web_static/current/
nginx_config="/etc/nginx/sites-available/default"
nginx_alias_config="location /hbnb_static/ {\n    alias /data/web_static/current/;\n}\n"

if ! grep -q 'location /hbnb_static/' "$nginx_config"; then
    sudo sed -i "/server_name _;/a $nginx_alias_config" "$nginx_config"
fi

# 7. Restart Nginx
sudo service nginx restart
