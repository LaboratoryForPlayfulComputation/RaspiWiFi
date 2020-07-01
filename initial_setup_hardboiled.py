import os
import sys
import setup_lib

'''
Creates the following directories/files via setup_lib.py:
- /usr/lib/raspiwifi
- /etc/raspiwifi
- changes /etc/wpa_supplicant.conf to /etc/wpa_supplicant.conf.original
- changes /etc/dnsmasq.conf to /etc/dnsmasq.conf.original
- copies lib/reset_device/dnsmasq.conf to /etc
- copies lib/reset_device/... to te corresponding /etc files
- creates a cron job for raspiwifi
- creates /etc/raspiwifi/host_mode

WARNING: DOES NOT CURRENTLY WORK IF YOU RE-RUN THIS FILE

'''


if os.getuid():
    sys.exit('You need root access to install!')


entered_ssid = ""
wpa_enabled_choice = "N"
wpa_entered_key = ""
auto_config_choice = "y"
auto_config_delay = "180"
server_port_choice = "80"
ssl_enabled_choice = "N"
install_ans = "y"

if(install_ans.lower() == 'y'):
	setup_lib.copy_configs(wpa_enabled_choice)
	setup_lib.update_main_config_file(entered_ssid, auto_config_choice, auto_config_delay, ssl_enabled_choice, server_port_choice, wpa_enabled_choice, wpa_entered_key)
else:
	sys.exit()

os.system('reboot')
