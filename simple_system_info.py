# simple_system_info.py

import platform
import psutil
import socket
from datetime import datetime

print("=== SYSTEM INFO ===")
print(f"Hostname:    {socket.gethostname()}")
print(f"OS:          {platform.system()} {platform.release()}")
print(f"CPU:         {platform.processor()}")
print(f"Cores:       {psutil.cpu_count(logical=True)}")
print(f"RAM:         {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
print(f"Disk:        {psutil.disk_usage('/').total / (1024 ** 3):.2f} GB total")
print(f"IP Address:  {socket.gethostbyname(socket.gethostname())}")
