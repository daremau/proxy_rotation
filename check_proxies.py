import threading
import queue

import requests

q = queue.Queue()
valid_proxies = []

with open('proxy_list.txt', 'r') as file:
  proxies = file.read().split('\n')
  for p in proxies:
    q.put(p)
file.close()

def check_proxies():
  global q
  while not q.empty():
    proxy = q.get()
    try:
      res = requests.get("http://ipinfo.io/json", proxies={"http": proxy, "https": proxy})
    except:
      continue
    
    if res.status_code == 200:
      valid_proxies.append(proxy)
      print(proxy)

for _ in range(10):
  threading.Thread(target=check_proxies).start()
