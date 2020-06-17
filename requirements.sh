# ./requirements.sh
# requirements for raspiwifi to run -- needs an internet connection to be installed
# should either be pre-installed on image or pi needs to be connected via ethernet on first boot
apt update
apt install python3 python3-rpi.gpio python3-pip dnsmasq hostapd -y
pip3 install flask pyopenssl
