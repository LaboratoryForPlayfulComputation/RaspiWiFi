# ./requirements.sh
apt update
apt install python3 python3-rpi.gpio python3-pip dnsmasq hostapd -y
pip3 install flask pyopenssl
