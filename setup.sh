# How to Setup : 
# cd /home/pi
# git clone https://github.com/zzeromin/RetroPie-Coin.git
# cd RetroPie-Coin/
# chmod 755 setup.sh
# sudo ./setup.sh

cd /home/pi/
git clone https://github.com/zzeromin/RetroPie-Coin.git
cd RetroPie-Coin/
cp coin.service /lib/systemd/system/
systemctl enable coin.service
echo "RetroPie-Coin setup complete."
echo "Python-rpi setup is starting now"
# apt-get update
apt-get -y install python-rpi.gpio
echo "System will reboot after 3 seconds"
sleep 3
reboot
