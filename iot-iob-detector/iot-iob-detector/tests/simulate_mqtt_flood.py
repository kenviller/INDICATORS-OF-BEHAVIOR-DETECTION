
import os
broker = "192.168.1.10"
for i in range(10):
    os.system(f"mosquitto_pub -h {broker} -t 'iot/device/cmd' -m 'hack_{i}'")
