import ipaddress

import requests
from bs4 import BeautifulSoup

def validate_ip_address(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
    
url = 'https://free-proxy-list.net/'
response = requests.get(url)
content = response.text

soup = BeautifulSoup(content, 'lxml')

trs = soup.find_all('tr')
ips = []

for tr in trs:
  td = tr.find('td')
  if td:
    td_text = td.get_text()
    if validate_ip_address(td_text):
       ip = td_text
       ips.append(ip)

with open('proxy_list.txt', 'w') as file:
   for ip in ips:
      file.write(str(ip) + '\n')