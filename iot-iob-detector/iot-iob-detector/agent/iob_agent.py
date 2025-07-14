
import time
import psutil
from utils.logger import log_alert
from config import trusted_ports, suspicious_threshold

def detect_anomalies():
    connections = psutil.net_connections(kind='inet')
    suspicious = 0
    for conn in connections:
        if conn.status == 'ESTABLISHED' and conn.raddr:
            port = conn.raddr.port
            if port not in trusted_ports:
                suspicious += 1
    return suspicious > suspicious_threshold

while True:
    if detect_anomalies():
        log_alert("⚠️ Abnormal outbound connections detected")
    time.sleep(30)
