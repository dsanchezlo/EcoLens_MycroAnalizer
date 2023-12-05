import os
import re

def get_connected_ssid():
    result = os.popen('netsh wlan show interfaces').read()
    matches = re.findall(r'SSID\s*:\s(.*)', result)
    if matches:
        return matches[0].strip()

ssid = get_connected_ssid()
if ssid is not None:
    print(f"Verbunden mit WLAN-SSID: {ssid}")
else:
    print("Der Computer ist nicht mit einem WLAN-Netzwerk verbunden.")

sequence = "EcoLensNUM"

# Check if ssid is contained in sequence
if sequence in ssid:
    print(f"Die Buchstabenfolge '{sequence}' ist in der Variable enthalten.")
else:
    print(f"Die Buchstabenfolge '{sequence}' ist nicht in der Variable enthalten.")

'''
import subprocess

def is_connected_to_wifi(ssid_partial):
    result = subprocess.run(['netsh', 'wlan', 'show interfaces'], capture_output=True, text=True)
    return ssid_partial in result.stdout

ssid_partial_to_check = "F.Sanchez 2.4"
if is_connected_to_wifi(ssid_partial_to_check):
    print("Der Computer ist mit einem WLAN verbunden, das die SSID-Teilübereinstimmung enthält.")
else:
    print("Der Computer ist nicht mit einem WLAN verbunden, das die SSID-Teilübereinstimmung enthält.")
'''
