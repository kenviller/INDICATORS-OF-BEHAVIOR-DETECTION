
import os

target = "192.168.1.0/24"
print(f"Simulating port scan on {target}...")
os.system(f"nmap -sS {target}")
