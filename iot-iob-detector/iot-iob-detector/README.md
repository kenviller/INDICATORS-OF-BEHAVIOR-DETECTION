
# Lightweight IoB Detection Agent for IoT

This project provides a minimal and efficient system to detect Indicators of Behavior (IoBs) in IoT devices. It identifies abnormal behaviors such as port scanning or unauthorized outbound connections using simple heuristics and logging mechanisms.

## 📁 Structure

- `agent/`: IoB detection agent code
- `tests/`: Attack simulation scripts (e.g., port scan, MQTT abuse)
- `utils/`: Logging utility
- `data/`: Baseline and abnormal behavior datasets, log output

## 🚀 How to Use

1. **Install dependencies:**
   ```bash
   pip install -r agent/requirements.txt
   ```

2. **Run the agent:**
   ```bash
   python agent/iob_agent.py
   ```

3. **Simulate attacks for testing:**
   ```bash
   python tests/simulate_portscan.py
   python tests/simulate_mqtt_flood.py
   ```

4. **Check alerts in:**
   ```
   data/iob_alerts.log
   ```

## ✅ Features

- Detects abnormal outbound connections
- Logs alerts locally
- Simulates realistic IoT attack behaviors

## 📌 Notes

- Designed to run on low-resource devices (e.g., Raspberry Pi, OpenWRT)
- Easily extensible to include TinyML or MQTT-based remote alerts
